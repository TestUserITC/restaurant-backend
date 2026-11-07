from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.dependencies import get_db, get_current_user
from app.models.user import User
from app.schemas.auth import LoginRequest, Token, PasswordResetRequest, PasswordResetConfirm
from app.schemas.restaurant import RegisterRequest
from app.schemas.user import UserResponse
from app.services import auth as auth_service
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(register_data: RegisterRequest, db: AsyncSession = Depends(get_db)):
    return await auth_service.create_new_restaurant(db, register_data)

@router.post("/login", response_model=Token)
async def login(login_data: LoginRequest, db: AsyncSession = Depends(get_db)):
    user = await auth_service.authenticate_user(db, login_data)
    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role
    }

@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/forgot-password", status_code=status.HTTP_200_OK)
async def forgot_password(request: PasswordResetRequest, db: AsyncSession = Depends(get_db)):
    # Simulate sending email, always return 200 OK for security reasons
    # to prevent email enumeration.
    await auth_service.request_password_reset_email(db, request.email)
    return {"message": "Te hemos enviado un link de recuperación a tu correo. Por favor, revisa tu bandeja de entrada"}

@router.post("/reset-password", status_code=status.HTTP_200_OK)
async def reset_password(request: PasswordResetConfirm, db: AsyncSession = Depends(get_db)):
    if request.new_password != request.confirm_new_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Las contraseñas no coinciden",
        )
    return await auth_service.reset_user_password(db, request)
