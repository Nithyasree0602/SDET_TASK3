🧪 Pytest Test Suite – User Data Handling & Validation

A lightweight test suite developed using the Pytest framework to validate user data management and input validation logic in a simulated backend environment. This project demonstrates unit and functional test writing capabilities, mimicking real-world SDET scenarios.

🔍 Task Objective

Develop unit and functional tests using the Pytest framework to:
   Test business logic for managing user data.
   Validate email and username fields using custom logic.
   Ensure robustness of the system through automated test coverage.

📦 Deliverables
File	Description
✅ data_manager.py	Contains the DataManager class responsible for CRUD operations on user data.
✅ sample_users.json	Mock JSON file with sample user data for testing.
✅ test_data_manager.py	Unit tests for DataManager functionality.
✅ test_user_validation.py	Tests for validating usernames and email formats.
✅ pytest.ini	Pytest configuration file for test discovery and module resolution.


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

🧠 Learnings & Highlights

Mastered use of pytest.mark.parametrize for efficient test coverage.
Gained hands-on debugging experience for common Pytest errors.
Applied clean code practices and modular test organization.
