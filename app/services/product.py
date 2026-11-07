from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_, func, or_
from fastapi import HTTPException, status
from datetime import datetime, timezone
from app.models.product import Product
from app.models.category import Category
from app.schemas.product import ProductCreate, ProductUpdate

async def get_products(db: AsyncSession, restaurant_id: int, category_id: int | None = None, search: str | None = None, skip: int = 0, limit: int = 100):
    """Get products with optional filtering by category and search"""
    query = select(Product).where(
        and_(
            Product.restaurant_id == restaurant_id,
            Product.deleted_at.is_(None)
        )
    )
    
    if category_id:
        query = query.where(Product.category_id == category_id)
    
    if search:
        query = query.where(
            or_(
                func.lower(Product.name).contains(func.lower(search)),
                func.lower(Product.description).contains(func.lower(search))
            )
        )
    
    query = query.order_by(Product.name).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def get_products_by_category(db: AsyncSession, restaurant_id: int, category_id: int):
    """Get all products in a specific category"""
    result = await db.execute(
        select(Product).where(
            and_(
                Product.restaurant_id == restaurant_id,
                Product.category_id == category_id,
                Product.deleted_at.is_(None)
            )
        ).order_by(Product.name)
    )
    return result.scalars().all()

async def create_product(db: AsyncSession, restaurant_id: int, product_data: ProductCreate):
    """Create a new product"""
    # Verify category exists and belongs to restaurant
    cat_result = await db.execute(
        select(Category).where(
            and_(
                Category.id == product_data.category_id,
                Category.restaurant_id == restaurant_id,
                Category.deleted_at.is_(None)
            )
        )
    )
    
    if not cat_result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La categoría seleccionada no existe"
        )
    
    product = Product(
        name=product_data.name,
        price=product_data.price,
        category_id=product_data.category_id,
        restaurant_id=restaurant_id,
        description=product_data.description,
        image_url=product_data.image_url,
        is_available=True
    )
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

async def update_product(db: AsyncSession, restaurant_id: int, product_id: int, product_data: ProductUpdate):
    """Update a product"""
    # Verify category exists
    cat_result = await db.execute(
        select(Category).where(
            and_(
                Category.id == product_data.category_id,
                Category.restaurant_id == restaurant_id,
                Category.deleted_at.is_(None)
            )
        )
    )
    
    if not cat_result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La categoría seleccionada no existe"
        )
    
    result = await db.execute(
        select(Product).where(
            and_(
                Product.id == product_id,
                Product.restaurant_id == restaurant_id,
                Product.deleted_at.is_(None)
            )
        )
    )
    
    product = result.scalars().first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    
    product.name = product_data.name
    product.price = product_data.price
    product.category_id = product_data.category_id
    product.description = product_data.description
    product.image_url = product_data.image_url
    
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

async def toggle_product_availability(db: AsyncSession, restaurant_id: int, product_id: int):
    """Toggle product availability"""
    result = await db.execute(
        select(Product).where(
            and_(
                Product.id == product_id,
                Product.restaurant_id == restaurant_id,
                Product.deleted_at.is_(None)
            )
        )
    )
    
    product = result.scalars().first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    
    product.is_available = not product.is_available
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product

async def delete_product(db: AsyncSession, restaurant_id: int, product_id: int):
    """Soft delete a product"""
    result = await db.execute(
        select(Product).where(
            and_(
                Product.id == product_id,
                Product.restaurant_id == restaurant_id,
                Product.deleted_at.is_(None)
            )
        )
    )
    
    product = result.scalars().first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    
    product.deleted_at = datetime.now(timezone.utc)
    db.add(product)
    await db.commit()
    return {"message": "Producto eliminado correctamente"}

async def count_products_in_category(db: AsyncSession, category_id: int) -> int:
    """Count active products in a category"""
    result = await db.execute(
        select(func.count()).select_from(Product).where(
            and_(
                Product.category_id == category_id,
                Product.deleted_at.is_(None)
            )
        )
    )
    return result.scalar() or 0
