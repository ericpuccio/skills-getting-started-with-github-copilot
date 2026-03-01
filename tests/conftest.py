import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def restore_activities():
    """Snapshot and restore the in-memory `activities` store around each test.

    This keeps tests isolated even though the app uses a module-level mutable
    data structure.
    """
    snapshot = copy.deepcopy(activities)
    try:
        yield
    finally:
        activities.clear()
        activities.update(snapshot)
