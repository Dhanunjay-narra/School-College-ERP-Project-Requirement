from writer_util import write_f
import subprocess

def create_base_files():
    write_f(".gitignore", """__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.env
.venv
build/
dist/
node_modules/
.DS_Store
*.log
local_data/
uploads/
""")

    write_f(".env.example", """ENVIRONMENT=development
APP_NAME=Enterprise School & College ERP
DEBUG=True
PORT=8000
API_PREFIX=/api/v1
SECRET_KEY=erp-enterprise-super-secure-production-key-2026-xyz
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_DAYS=7
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=school_college_erp
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/school_college_erp
REDIS_URL=redis://localhost:6379/0
""")

    write_f("LICENSE", """PROPRIETARY AND CONFIDENTIAL
Copyright (c) 2026 School/College ERP Platform. All Rights Reserved.
""")

    write_f("requirements.txt", """fastapi>=0.110.0
uvicorn[standard]>=0.28.0
pydantic>=2.6.4
pydantic-settings>=2.2.1
sqlalchemy>=2.0.28
alembic>=1.13.1
asyncpg>=0.29.0
psycopg2-binary>=2.9.9
redis>=5.0.3
celery>=5.3.6
python-jose[cryptography]>=3.3.0
passlib[bcrypt,argon2]>=1.7.4
bcrypt>=4.1.2
pyjwt>=2.8.0
python-multipart>=0.0.9
email-validator>=2.1.1
httpx>=0.27.0
pytest>=8.1.1
pytest-asyncio>=0.23.6
pytest-cov>=4.1.0
""")

    write_f("pyproject.toml", """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "school-college-erp"
version = "1.0.0"
description = "Enterprise Unified School and College ERP Platform"
readme = "README.md"
authors = [{ name = "ERP Engineering Team", email = "engineering@erp.edu" }]
dependencies = [
    "fastapi>=0.110.0",
    "uvicorn>=0.28.0",
    "pydantic>=2.6.4",
    "sqlalchemy>=2.0.28",
    "asyncpg>=0.29.0",
    "redis>=5.0.3",
    "pytest>=8.1.1"
]
""")

if __name__ == '__main__':
    create_base_files()
