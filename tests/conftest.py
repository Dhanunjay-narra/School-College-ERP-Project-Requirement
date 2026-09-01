"""
Global Pytest Configuration and Test Fixtures.
"""
import pytest
import asyncio
from typing import AsyncGenerator
from fastapi.testclient import TestClient
from backend.main import app
from backend.identity.infrastructure.repositories import InMemoryUserRepository, InMemoryRoleRepository
from backend.identity.application.services import AuthenticationService

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def client() -> TestClient:
    return TestClient(app)

@pytest.fixture
def auth_service():
    role_repo = InMemoryRoleRepository()
    user_repo = InMemoryUserRepository(role_repo)
    return AuthenticationService(user_repo, role_repo)
