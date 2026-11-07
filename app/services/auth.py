from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.user import User, UserRole
from app.models.restaurant import Restaurant
from app.models.branch import Branch
from app.schemas.auth import LoginRequest, PasswordResetConfirm
from app.schemas.restaurant import RegisterRequest
from app.core.security import (
    verify_password, get_password_hash, create_access_token,
    create_password_reset_token, verify_password_reset_token
)

async def authenticate_user(db: AsyncSession, login_data: LoginRequest):
    result = await db.execute(select(User).where(User.email == login_data.email))
    user = result.scalars().first()

    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario inactivo",
        )

    return user

async def create_new_restaurant(db: AsyncSession, register_data: RegisterRequest):
    # Check if email exists
    result = await db.execute(select(User).where(User.email == register_data.email))
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este email ya está en uso. Por favor, usa otro email o inicia sesión",
        )

    if not register_data.accept_terms:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Debes aceptar los términos y condiciones",
        )

    # 1. Create Restaurant
    restaurant = Restaurant(
        name=register_data.restaurant_name,
        address=register_data.address
    )
    db.add(restaurant)
    await db.flush() # Get restaurant ID

    # 2. Create Default Branch
    branch = Branch(
        name="Principal",
        address=register_data.address,
        restaurant_id=restaurant.id
    )
    db.add(branch)

    # 3. Create Owner User
    user = User(
        email=register_data.email,
        hashed_password=get_password_hash(register_data.password),
        full_name=register_data.full_name,
        role=UserRole.OWNER,
        restaurant_id=restaurant.id
    )
    db.add(user)

    await db.commit()
    await db.refresh(user)
    return user

async def request_password_reset_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()

    if user:
        reset_token, expires_at = create_password_reset_token()
        user.password_reset_token = reset_token
        user.password_reset_token_expires_at = expires_at
        db.add(user)
        await db.commit()
        await db.refresh(user)

        # Simulate sending email
        reset_link = f"http://localhost:8000/reset-password?token={reset_token}"
        print(f"\n--- SIMULATED EMAIL ---")
        print(f"To: {user.email}")
        print(f"Subject: Recuperación de contraseña - Restaurant Management System")
        print(f"Body:\n")
        print(f"Hola {user.full_name},\n")
        print(f"Has solicitado restablecer tu contraseña para el Restaurant Management System.")
        print(f"Haz clic en el siguiente enlace para establecer una nueva contraseña:\n")
        print(f"{reset_link}\n")
        print(f"Este enlace es válido por 1 hora.\n")
        print(f"Si no solicitaste este cambio, ignora este email.\n")
        print(f"Saludos,\nEl equipo de Restaurant Management System")
        print(f"-----------------------\n")
    # Always return success to prevent email enumeration
    return {"message": "Te hemos enviado un link de recuperación a tu correo. Por favor, revisa tu bandeja de entrada"}

async def reset_user_password(db: AsyncSession, token_data: PasswordResetConfirm):
    result = await db.execute(select(User).where(User.password_reset_token == token_data.token))
    user = result.scalars().first()

    if not user or not verify_password_reset_token(token_data.token, user.password_reset_token, user.password_reset_token_expires_at):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Este link de recuperación no es válido o ha expirado. Por favor, solicita uno nuevo",
        )

    user.hashed_password = get_password_hash(token_data.new_password)
    user.password_reset_token = None  # Invalidate token after use
    user.password_reset_token_expires_at = None
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return {"message": "Tu contraseña ha sido actualizada exitosamente"}
