
from src.data_manager import DataManager

def test_get_user_by_id():
    dm = DataManager("data/sample_users.json")
    assert dm.get_user_by_id("nithya_sree") is not None

def test_get_user_by_id_not_found():
    dm = DataManager("data/sample_users.json")
    assert dm.get_user_by_id("non_existing_user") is None

def test_count_users_with_email():
    dm = DataManager("data/sample_users.json")
    assert dm.count_users_with_email("@example.com") == 2
