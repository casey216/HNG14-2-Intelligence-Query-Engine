import os
os.environ["TESTING"] = "1"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.server import app
import app.db.database as db_module
from app.db.database import init_db, get_db, Base


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """Initializes in-memory test DB once for the whole test session"""
    init_db(test=True)
    Base.metadata.create_all(bind=db_module.engine)
    yield
    Base.metadata.drop_all(bind=db_module.engine)


@pytest.fixture(scope="function")
def db_session(setup_test_db):
    """Yields a DB session that rolls back after each test"""
    with db_module.engine.connect() as connection:

        with Session(connection) as session:
            yield session
            session.rollback()

            for table in reversed(Base.metadata.sorted_tables):
                connection.execute(table.delete())
            connection.commit()


@pytest.fixture(scope="function")
def client(db_session):
    """FASTApi Test client with DB dependency overridden."""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()