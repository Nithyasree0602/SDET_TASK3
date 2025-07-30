import pytest
import json

@pytest.fixture(scope="module")
def sample_user_data():
    with open("data/sample_users.json") as f:
        return json.load(f)
