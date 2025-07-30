🔍 Task Objective

Develop unit and functional tests using the Pytest framework for validating user data handling and user input validation logic.

📦 Deliverables

✅ data_manager.py – DataManager class with methods to handle user data.

✅ sample_users.json – JSON file with mock user data.

✅ test_data_manager.py – Test cases to verify DataManager functionality.

✅ test_user_validation.py – Test cases for validating username and email logic.

✅ pytest.ini – Pytest configuration file.

✅ Clean, passing Pytest report:

5 passed, 0 failed, 0 warnings

⚠️ Errors Faced & How I Resolved Them 
1. ImportError – src.data_manager not found
Issue: Pytest couldn’t locate the data_manager.py module.

  Fix:
  Added __init__.py to both src/ and tests/ folders.

  Appended project root to sys.path in test files:
  import sys, os  
  sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


2. AssertionError – User not found
Issue: get_user_by_id("nithya_sree") returned None.

  Fix:
  Updated sample_users.json to include:


  {
    "user_id": "nithya_sree",
    "name": "Nithya",
    "email": "nithya@example.com"
  }

3. Syntax Warning – Pytest config warning
Issue: Pytest raised warnings about missing config for test discovery.

  Fix:
  Created a pytest.ini file:

  [pytest]
  python_files = test_*.py
  pythonpath = .
  "# SDET_TASK3" 
