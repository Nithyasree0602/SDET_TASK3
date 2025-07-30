import json

class DataManager:
    def __init__(self, json_path):
        with open(json_path) as f:
            self.data = json.load(f)

    def get_user_by_id(self, user_id):
        return next((u for u in self.data if u["id"] == user_id), None)

    def count_users_with_email(self, domain):
        return sum(1 for u in self.data if domain in u["email"])
