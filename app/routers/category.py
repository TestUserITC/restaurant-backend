from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func, and_
from app.dependencies import get_db, get_current_active_owner
from app.models.user import User
from app.models.product import Product
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse, CategoryListResponse
from app.services import category as category_service

router = APIRouter(prefix="/menu", tags=["Menu - Categories"])

@router.get("/categories", response_model=list[CategoryListResponse])
async def get_categories(
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Get all active categories for the restaurant (Owner only)"""
    categories = await category_service.get_categories(db, current_user.restaurant_id)
    
    # Build response with product counts
    result = []
    for cat in categories:
        product_count = await db.execute(
            select(func.count()).select_from(Product).where(
                and_(
                    Product.category_id == cat.id,
                    Product.deleted_at.is_(None)
                )
            )
        )
        count = product_count.scalar() or 0
        result.append({
            "id": cat.id,
            "name": cat.name,
            "is_active": cat.is_active,
            "product_count": count,
            "created_at": cat.created_at
        })
    
    return result

@router.post("/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    category_data: CategoryCreate,
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Create a new category (Owner only)"""
    return await category_service.create_category(db, current_user.restaurant_id, category_data)

@router.put("/categories/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Update a category (Owner only)"""
    return await category_service.update_category(db, current_user.restaurant_id, category_id, category_data)

@router.patch("/categories/{category_id}/toggle", response_model=CategoryResponse)
async def toggle_category(
    category_id: int,
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Toggle category active/inactive status (Owner only)"""
    return await category_service.toggle_category_status(db, current_user.restaurant_id, category_id)

@router.delete("/categories/{category_id}", status_code=status.HTTP_200_OK)
async def delete_category(
    category_id: int,
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Delete a category (soft delete, Owner only)"""
    return await category_service.delete_category(db, current_user.restaurant_id, category_id)
