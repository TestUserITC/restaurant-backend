from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.core.database import engine, Base
from app.routers import auth, category, product, order, sales, pos, settings, dashboard
# Import models to ensure they are registered with Base.metadata
from app.models import User, Restaurant, Branch, Category, Product, Order, OrderItem, RestaurantSettings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # The project has no migrations: tables are created on startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="Restaurant Management System API",
    description="SaaS Restaurant Management System MVP API",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(auth.router)
app.include_router(category.router)
app.include_router(product.router)
app.include_router(order.router)
app.include_router(sales.router)
app.include_router(pos.router)
app.include_router(settings.router)
app.include_router(dashboard.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Restaurant Management System API",
        version="0.1.0",
        description="SaaS Restaurant Management System MVP API",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "HTTPBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    
    # Add security to all paths except /auth/register and /auth/login and /health
    for path, path_item in openapi_schema["paths"].items():
        for method, operation in path_item.items():
            if method in ["get", "post", "put", "patch", "delete"]:
                if path not in ["/auth/register", "/auth/login", "/health"] and not path.startswith("/auth/forgot") and not path.startswith("/auth/reset"):
                    if "security" not in operation:
                        operation["security"] = [{"HTTPBearer": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": "Restaurant Backend is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
