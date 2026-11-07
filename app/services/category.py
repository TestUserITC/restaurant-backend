from datetime import timezone

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_, func
from fastapi import HTTPException, status
from app.models.category import Category
from app.models.user import User
from app.schemas.category import CategoryCreate, CategoryUpdate

async def get_categories(db: AsyncSession, restaurant_id: int):
    """Get all active categories for a restaurant, ordered alphabetically"""
    result = await db.execute(
        select(Category)
        .where(
            and_(
                Category.restaurant_id == restaurant_id,
                Category.deleted_at.is_(None)
            )
        )
        .order_by(Category.name)
    )
    categories = result.scalars().all()
    
    # Add product count to each category
    from app.models.product import Product
    categories_with_count = []
    for cat in categories:
        product_count_result = await db.execute(
            select(func.count()).select_from(Product).where(
                and_(
                    Product.category_id == cat.id,
                    Product.deleted_at.is_(None)
                )
            )
        )
        count = product_count_result.scalar() or 0
        cat.product_count = count
        categories_with_count.append(cat)
    
    return categories_with_count

async def create_category(db: AsyncSession, restaurant_id: int, category_data: CategoryCreate):
    """Create a new category with name uniqueness check"""
    # Check if category name already exists (case-insensitive)
    result = await db.execute(
        select(Category).where(
            and_(
                Category.restaurant_id == restaurant_id,
                func.lower(Category.name) == func.lower(category_data.name),
                Category.deleted_at.is_(None)
            )
        )
    )
    
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una categoría con este nombre"
        )
    
    category = Category(
        name=category_data.name,
        restaurant_id=restaurant_id,
        is_active=True
    )
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category

async def update_category(db: AsyncSession, restaurant_id: int, category_id: int, category_data: CategoryUpdate):
    """Update a category with name uniqueness check"""
    result = await db.execute(
        select(Category).where(
            and_(
                Category.id == category_id,
                Category.restaurant_id == restaurant_id,
                Category.deleted_at.is_(None)
            )
        )
    )
    
    category = result.scalars().first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada"
        )
    
    # Check if new name already exists (excluding current category)
    if category.name.lower() != category_data.name.lower():
        dup_result = await db.execute(
            select(Category).where(
                and_(
                    Category.restaurant_id == restaurant_id,
                    func.lower(Category.name) == func.lower(category_data.name),
                    Category.deleted_at.is_(None),
                    Category.id != category_id
                )
            )
        )
        
        if dup_result.scalars().first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe una categoría con este nombre"
            )
    
    category.name = category_data.name
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category

async def toggle_category_status(db: AsyncSession, restaurant_id: int, category_id: int):
    """Toggle category active/inactive status"""
    result = await db.execute(
        select(Category).where(
            and_(
                Category.id == category_id,
                Category.restaurant_id == restaurant_id,
                Category.deleted_at.is_(None)
            )
        )
    )
    
    category = result.scalars().first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada"
        )
    
    category.is_active = not category.is_active
    db.add(category)
    await db.commit()
    await db.refresh(category)
    return category

async def delete_category(db: AsyncSession, restaurant_id: int, category_id: int):
    """Soft delete a category (only if it has no products)"""
    result = await db.execute(
        select(Category).where(
            and_(
                Category.id == category_id,
                Category.restaurant_id == restaurant_id,
                Category.deleted_at.is_(None)
            )
        )
    )
    
    category = result.scalars().first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoría no encontrada"
        )
    
    # Check if category has products (will implement when Product model exists)
    # For now, we'll allow deletion
    from datetime import datetime
    from sqlalchemy import timezone as sql_timezone
    
    category.deleted_at = datetime.now(timezone.utc)
    db.add(category)
    await db.commit()
    return {"message": "Categoría eliminada correctamente"}
