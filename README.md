# Restaurant Backend

REST API for a restaurant management SaaS (MVP): authentication, menu, orders, point of sale, sales reporting and per-restaurant settings. Every record belongs to a restaurant, and users only see data from their own.

## Stack

- Python 3.11+, FastAPI, Pydantic v2
- PostgreSQL 16, SQLAlchemy 2 (async) with asyncpg
- JWT bearer authentication (python-jose, passlib/bcrypt)

## Getting started

### With Docker

```bash
cp .env.example .env
docker compose up --build
```

### Without Docker

Requires Python 3.11+ and a PostgreSQL instance. `docker compose up -d db` starts one.

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs at `http://localhost:8000`, with interactive documentation at `/docs`. Tables are created on startup; there are no migrations.

## Configuration

| Variable | Required | Description |
| --- | --- | --- |
| `DATABASE_URL` | Yes | Async connection string (`postgresql+asyncpg://...`). Compose overrides the host with `db` for the API container. |
| `SECRET_KEY` | Yes | JWT signing key. |
| `ALGORITHM` | No | JWT algorithm. Default: `HS256`. |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | No | Token lifetime. Default: `30`. |
| `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` | Compose only | Credentials for the database container. Keep them in sync with `DATABASE_URL`. |

## Project structure

```
app/
  main.py          Application entry point and router registration
  dependencies.py  Shared dependencies: database session, current user, role checks
  core/            Settings, database engine, security helpers
  models/          SQLAlchemy models
  schemas/         Pydantic request and response schemas
  routers/         HTTP layer
  services/        Business logic
docs/
  epicas/          Functional requirements by epic (Spanish)
  user-stories/    The same requirements split per user story (Spanish)
```

Requests flow `router -> service -> model`. Validation belongs in schemas and business rules in services. API error messages are in Spanish.

## API

All endpoints require `Authorization: Bearer <token>` except `/health`, `/auth/register`, `/auth/login`, `/auth/forgot-password` and `/auth/reset-password`.

| Area | Endpoints | Access |
| --- | --- | --- |
| Health | `GET /health` | Public |
| Auth | `POST /auth/register`, `POST /auth/login`, `POST /auth/forgot-password`, `POST /auth/reset-password` | Public |
| Auth | `GET /auth/me` | Any user |
| Categories | `GET`, `POST /menu/categories`; `PUT`, `DELETE /menu/categories/{id}`; `PATCH /menu/categories/{id}/toggle` | Owner |
| Products | `GET`, `POST /menu/products`; `PUT`, `DELETE /menu/products/{id}`; `PATCH /menu/products/{id}/toggle` | Owner |
| Orders | `GET`, `POST /orders`; `GET /orders/stats`; `GET /orders/{id}`; `PATCH /orders/{id}/status`; `PATCH /orders/{id}/notes` | Any user |
| POS | `GET /pos/products`, `GET /pos/categories` | Any user |
| Sales | `GET /sales/history`, `GET /sales/statistics`, `GET /sales/today` | Owner |
| Settings | `GET`, `PATCH /settings` | Owner |
| Dashboard | `GET /dashboard/owner` | Owner |
| Dashboard | `GET /dashboard/cashier` | Any user |

### First requests

Registering creates the restaurant, a default branch and an owner user:

```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"restaurant_name": "Demo Restaurant", "full_name": "Demo Owner", "email": "owner@example.com", "password": "password123", "confirm_password": "password123", "accept_terms": true}'

curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "owner@example.com", "password": "password123"}'
```

## Domain rules

- **Roles:** `owner` has full access; `cashier` has operational access. Registration only creates owners, and no endpoint creates cashiers yet.
- **Order lifecycle:** `pending -> in_preparation -> ready -> closed`. Any other transition returns `400`. Closed orders count as sales.
- **Historical data:** orders store a snapshot of the tax rate, product name and unit price, so later menu or settings changes do not alter past sales.
- **Soft delete:** categories and products are marked with `deleted_at`, never removed.
- **Money:** use `Decimal`, never `float`.
- **Tax rate:** stored as a fraction. The default is `0.18`, meaning 18%.
- **Password recovery:** no email provider is integrated; the reset link is printed to the server log.

## Testing

There is no automated test suite yet.

## Known issues

| Area | Problem |
| --- | --- |
| Orders, sales | `POST /orders`, `GET /orders`, `GET /orders/{id}`, both `PATCH /orders/{id}/...` endpoints and `GET /sales/history` return `500` because `Order.items` is lazy-loaded outside the async context. Write operations are saved before the error is raised. |
| Orders | `order_number` is unique across all restaurants but numbered per restaurant, so a second restaurant's first order fails with `500`. |
| Dashboard | `GET /dashboard/owner` always returns `500`: the top-products query joins `Product` to `Order` directly, and they are only related through `OrderItem`. |
| Dashboard | `GET /dashboard/cashier` reports all open orders as `pending_orders`, not only the pending ones. |
| Auth | `POST /auth/reset-password` returns `500` when comparing a timezone-aware date with the stored naive one. |
| Settings | `PATCH /settings` accepts `tax_rate` values up to `100`, but the rate is applied as a fraction: `18` produces an 1800% tax. |
