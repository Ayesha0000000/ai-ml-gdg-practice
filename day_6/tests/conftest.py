import os
import sys

# ✅ Set environment variables BEFORE importing app
os.environ["API_KEY"] = "test-key"
os.environ["APP_NAME"] = "Test API"
os.environ["ENVIRONMENT"] = "test"
os.environ["DEBUG"] = "false"

# ✅ Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import pytest
from fastapi.testclient import TestClient

from git_day_practice.api import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
