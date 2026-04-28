# FastAPI Skeleton

A production-ready skeleton for building backend services with **FastAPI** and **PostgreSQL**. Clone this repo and start adding features — the boring setup is already done.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | [FastAPI](https://fastapi.tiangolo.com/) `^0.115` |
| ASGI Server | [Uvicorn](https://www.uvicorn.org/) |
| ORM | [SQLAlchemy](https://www.sqlalchemy.org/) `2.0` |
| Database | PostgreSQL |
| Migrations | [Alembic](https://alembic.sqlalchemy.org/) |
| Package Manager | [Poetry](https://python-poetry.org/) |
| Containerization | Docker |

---

## Project Structure

```
src/
├── app.py                  # FastAPI instance, routers, middleware
├── core/
│   └── config.py           # Environment-based configuration
├── api/
│   ├── api_v1/             # API version 1 routers
│   └── api_v2/             # API version 2 routers
├── models/
│   ├── base.py             # Base ORM model (id, created_at, updated_at)
│   └── user.py             # User model
├── schemas/
│   └── users.py            # Pydantic request/response schemas
├── services/
│   └── users/              # Business logic
├── db/
│   ├── db.py               # Engine, session factory
│   └── migrations/         # Alembic migration scripts
└── utils/
    └── time.py             # Datetime helpers
```

---

## Prerequisites

- Python `3.9.9`
- PostgreSQL (running locally or via Docker)
- [Poetry](https://python-poetry.org/docs/#installation)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-skeleton.git
cd fastapi-skeleton
```

### 2. Configure environment variables

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

Key variables to set:

```dotenv
APP_NAME=my-fastapi-app
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=false

DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_NAME=your_db

SECRET_KEY=your-secret-key-here
REFRESH_SECRET_KEY=your-refresh-secret-key-here
TOKEN_EXPIRATION=86400
REFRESH_TOKEN_EXPIRATION=2592000
```

> **Note:** Never commit your `.env` file. It is already listed in `.gitignore`.

### 3. Install dependencies

```bash
export LANG="en_US.UTF-8"
poetry shell
poetry install --no-root
```

### 4. Run database migrations

```bash
alembic upgrade head
```

### 5. Start the development server

```bash
uvicorn src.app:fast_api --host 0.0.0.0 --port 8000 --reload --log-level debug
```

The API will be available at:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`
- **Health check:** `http://localhost:8000/health`

---

## Environment Variables Reference

| Variable | Default | Description |
|---|---|---|
| `APP_NAME` | `My Fast API app` | Application name shown in health check |
| `APP_HOST` | `0.0.0.0` | Host the server binds to |
| `APP_PORT` | `8000` | Port the server listens on |
| `DEBUG` | `false` | Enable SQLAlchemy query logging |
| `DATABASE_DRIVER` | `postgresql+psycopg2` | SQLAlchemy database driver |
| `DATABASE_HOST` | `localhost` | Database hostname |
| `DATABASE_PORT` | `5432` | Database port |
| `DATABASE_USER` | `postgres` | Database username |
| `DATABASE_PASSWORD` | — | Database password |
| `DATABASE_NAME` | `postgres` | Database name |
| `SECRET_KEY` | — | JWT signing secret |
| `REFRESH_SECRET_KEY` | — | JWT refresh token secret |
| `TOKEN_EXPIRATION` | `86400` | Access token TTL in seconds (24h) |
| `REFRESH_TOKEN_EXPIRATION` | `2592000` | Refresh token TTL in seconds (30d) |

---

## Database Migrations

Create a new migration after changing a model:

```bash
alembic revision --autogenerate -m "describe your change here"
```

Apply pending migrations:

```bash
alembic upgrade head
```

Roll back the last migration:

```bash
alembic downgrade -1
```

---

## Adding a New Feature

When building a new domain (e.g. `products`), follow this pattern:

1. **Model** — add `src/models/product.py` extending `BaseModel`
2. **Schema** — add `src/schemas/products.py` with request/response Pydantic models
3. **Service** — add `src/services/products/` with business logic
4. **Router** — add `src/api/api_v1/products.py` and register it in `app.py`
5. **Migration** — run `alembic revision --autogenerate -m "add products table"`

---

## API Versioning

Routers are versioned under `/api/v1` and `/api/v2`. Only create a new version when introducing a **breaking change** to an existing endpoint — do not duplicate code.

---

## Docker

### Build the image

```bash
docker build -t <IMAGE_NAME> --progress=plain -f Dockerfile . 2>&1 | tee docker_build.log
```

### Run the container

```bash
docker run \
  --network <CONTAINER_NETWORK> \
  -p <EXTERNAL_PORT>:<APP_PORT> \
  --env-file .env \
  --name <CONTAINER_NAME> \
  -d <IMAGE_NAME>
```

**Example:**

```bash
docker run \
  --network host \
  -p 8000:8000 \
  --env-file .env \
  --name fastapi-app \
  -d fastapi-skeleton
```

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push the branch: `git push origin feat/your-feature`
5. Open a Pull Request

Please make sure to update tests as appropriate.

---

## License

[MIT](https://choosealicense.com/licenses/mit/)
