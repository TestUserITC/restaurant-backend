from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_active_owner
from app.models.user import User
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse, ProductListResponse
from app.services import product as product_service

router = APIRouter(prefix="/menu", tags=["Menu - Products"])

@router.get("/products", response_model=list[ProductListResponse])
async def get_products(
    category_id: int | None = Query(None),
    search: str | None = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Get products with optional filtering by category and search (Owner only)"""
    products = await product_service.get_products(
        db, current_user.restaurant_id, category_id, search, skip, limit
    )
    
    # Enrich with category names
    from sqlalchemy.future import select
    from sqlalchemy import and_
    from app.models.category import Category
    
    enriched = []
    for product in products:
        cat_result = await db.execute(
            select(Category).where(Category.id == product.category_id)
        )
        category = cat_result.scalars().first()
        enriched.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "category_id": product.category_id,
            "category_name": category.name if category else "",
            "is_available": product.is_available,
            "image_url": product.image_url,
            "created_at": product.created_at
        })
    
    return enriched

@router.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_data: ProductCreate,
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Create a new product (Owner only)"""
    return await product_service.create_product(db, current_user.restaurant_id, product_data)

@router.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product_data: ProductUpdate,
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Update a product (Owner only)"""
    return await product_service.update_product(db, current_user.restaurant_id, product_id, product_data)

@router.patch("/products/{product_id}/toggle", response_model=ProductResponse)
async def toggle_product(
    product_id: int,
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Toggle product availability (Owner only)"""
    return await product_service.toggle_product_availability(db, current_user.restaurant_id, product_id)

@router.delete("/products/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product(
    product_id: int,
    current_user: User = Depends(get_current_active_owner),
    db: AsyncSession = Depends(get_db)
):
    """Delete a product (soft delete, Owner only)"""
    return await product_service.delete_product(db, current_user.restaurant_id, product_id)
