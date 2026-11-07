from typing import AsyncGenerator
from fastapi import Depends, HTTPException, status
from fastapi.security.http import HTTPBearer
from starlette.requests import Request
from jose import jwt, JWTError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import SessionLocal
from app.core.config import settings
from app.models.user import User, UserRole
from app.schemas.auth import TokenData

security = HTTPBearer()

async def get_db() -> AsyncGenerator:
    async with SessionLocal() as session:
        yield session

async def get_current_user(
    request: Request,
    db: AsyncSession = Depends(get_db)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise credentials_exception
    
    token = auth_header.split(" ")[1]
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

    result = await db.execute(select(User).where(User.email == token_data.email))
    user = result.scalars().first()
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_owner(
    request: Request,
    db: AsyncSession = Depends(get_db)
) -> User:
    user = await get_current_user(request=request, db=db)
    if user.role != UserRole.OWNER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para acceder a esta sección",
        )
    return user


async def get_current_active_cashier(
    request: Request,
    db: AsyncSession = Depends(get_db)
) -> User:
    user = await get_current_user(request=request, db=db)
    if user.role not in [UserRole.CASHIER, UserRole.OWNER]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para acceder a esta sección",
        )
    return user
