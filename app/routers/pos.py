from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from decimal import Decimal
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.models.product import Product
from app.models.category import Category

router = APIRouter(prefix="/pos", tags=["POS"])

@router.get("/products", response_model=list[dict])
async def get_pos_products(
    category_id: int | None = Query(None, description="Filter by category ID"),
    search: str | None = Query(None, description="Search by product name"),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get products for POS interface with categories (Owner & Cashier)"""
    query = select(Product).where(
        and_(
            Product.restaurant_id == current_user.restaurant_id,
            Product.deleted_at.is_(None)
        )
    )
    
    if category_id:
        query = query.where(Product.category_id == category_id)
    
    if search:
        from sqlalchemy import func
        query = query.where(func.lower(Product.name).contains(func.lower(search)))
    
    query = query.order_by(Product.name)
    result = await db.execute(query)
    products = result.scalars().all()
    
    # Enrich with category names
    result_list = []
    for product in products:
        cat_result = await db.execute(
            select(Category).where(Category.id == product.category_id)
        )
        category = cat_result.scalars().first()
        result_list.append({
            "id": product.id,
            "name": product.name,
            "price": float(product.price),
            "category_id": product.category_id,
            "category_name": category.name if category else "",
            "is_available": product.is_available,
            "image_url": product.image_url
        })
    
    return result_list

@router.get("/categories", response_model=list[dict])
async def get_pos_categories(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get active categories for POS (Owner & Cashier)"""
    query = select(Category).where(
        and_(
            Category.restaurant_id == current_user.restaurant_id,
            Category.deleted_at.is_(None),
            Category.is_active == True
        )
    ).order_by(Category.name)
    
    result = await db.execute(query)
    categories = result.scalars().all()
    
    return [
        {
            "id": cat.id,
            "name": cat.name
        }
        for cat in categories
    ]
