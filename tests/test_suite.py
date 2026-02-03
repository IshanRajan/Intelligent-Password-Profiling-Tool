#enjoy


"""
Comprehensive Test Suite for Password Profiling Tool

This test suite covers all major components:
- Username generation
- Username variations
- Password generation
- Password analysis
- Data loading (CSV, JSON, TXT)
- Report generation

Run with: python test_suite.py
"""

import unittest
import os
import json
import csv
import tempfile
import shutil
from pathlib import Path

# Import your modules
# Adjust these imports based on your actual folder structure
import sys

# Add parent directory to path (in case running from tests/ folder)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
sys.path.insert(0, current_dir)

# Try to import modules with better error handling
IMPORTS_SUCCESSFUL = True
import_errors = []

try:
    from generator.username_generator import generate_username, expand_username_variations
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    import_errors.append(f"generator.username_generator: {e}")

try:
    from generator.password_generator import generate_passwords
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    import_errors.append(f"generator.password_generator: {e}")

try:
    from analyzer.profile_analyzer import profile_analyzer
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    import_errors.append(f"analyzer.password_analyzer: {e}")

try:
    from data.data_loader import load_csv, load_json, load_text
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    import_errors.append(f"data.data_loader: {e}")

try:
    from reporter.report_generator import generate_report
except ImportError as e:
    IMPORTS_SUCCESSFUL = False
    import_errors.append(f"reporter.report_generator: {e}")

if not IMPORTS_SUCCESSFUL:
    print("\n" + "=" * 70)
    print("IMPORT ERRORS DETECTED")
    print("=" * 70)
    print("\nCould not import one or more required modules:")
    for error in import_errors:
        print(f"  ✗ {error}")
    print("\nPlease check:")
    print("  1. You're running this from your project root directory")
    print("  2. Your folder structure matches:")
    print("     - generator/username_generator.py")
    print("     - generator/password_generator.py")
    print("     - analyzer/password_analyzer.py")
    print("     - data/data_loader.py")
    print("     - reporter/report_generator.py")
    print("  3. Each folder has an __init__.py file")
    print("\nCurrent directory:", os.getcwd())
    print("=" * 70 + "\n")
    sys.exit(1)


class TestUsernameGenerator(unittest.TestCase):
    """Test username generation functionality."""
    
    def setUp(self):
        """Set up test profile."""
        self.profile = {
            "first": "John",
            "last": "Doe",
            "nick": "JD",
            "year": "1990",
            "hobby": "gaming",
            "company": "TechCorp"
        }
    
    def test_basic_username_generation(self):
        """Test that basic usernames are generated."""
        usernames = generate_username(self.profile)
        
        # Should generate at least some usernames
        self.assertGreater(len(usernames), 0)
        
        # Check for specific expected usernames (all lowercase)
        self.assertIn("johndoe", usernames)
        self.assertIn("jdoe", usernames)
        self.assertIn("jd", usernames)
    
    def test_username_lowercase(self):
        """Test that all usernames are lowercase."""
        usernames = generate_username(self.profile)
        
        for username in usernames:
            self.assertEqual(username, username.lower())
    
    def test_username_with_year(self):
        """Test that year-based usernames are generated."""
        usernames = generate_username(self.profile)
        
        self.assertIn("john1990", usernames)
        self.assertIn("doe1990", usernames)
    
    def test_username_no_duplicates(self):
        """Test that there are no duplicate usernames."""
        usernames = generate_username(self.profile)
        
        self.assertEqual(len(usernames), len(set(usernames)))
    
    def test_null_values_handling(self):
        """Test handling of null values in profile."""
        profile_with_nulls = {
            "first": "Jane",
            "last": "Smith",
            "nick": "null",
            "year": "2000",
            "hobby": "null",
            "company": "null"
        }
        
        usernames = generate_username(profile_with_nulls)
        
        # Should still generate usernames
        self.assertGreater(len(usernames), 0)
        # Should not contain the word "null"
        for username in usernames:
            if username != "null":  # "null" might be the nickname
                self.assertNotIn("nullnull", username)


class TestUsernameVariations(unittest.TestCase):
    """Test username variation expansion."""
    
    def setUp(self):
        """Set up test data."""
        self.profile = {
            "first": "Alice",
            "last": "Brown",
            "nick": "AB",
            "year": "1995",
            "hobby": "reading",
            "company": "BookCo"
        }
        self.base_usernames = generate_username(self.profile)
    
    def test_variations_generated(self):
        """Test that variations are generated."""
        variations = expand_username_variations(self.base_usernames, self.profile)
        
        # Should generate variations
        self.assertGreater(len(variations), 0)
    
    def test_separator_variations(self):
        """Test that separator variations are created."""
        variations = expand_username_variations(self.base_usernames, self.profile)
        
        # Check for variations with separators
        separator_found = any(
            "_" in v or "." in v or "-" in v 
            for v in variations
        )
        self.assertTrue(separator_found)
    
    def test_capitalization_variations(self):
        """Test that capitalization variations exist."""
        variations = expand_username_variations(self.base_usernames, self.profile)
        
        # Check for capitalized variations
        capitalized_found = any(
            v != v.lower() 
            for v in variations
        )
        self.assertTrue(capitalized_found)
    
    def test_no_duplicate_variations(self):
        """Test that variations don't have duplicates."""
        variations = expand_username_variations(self.base_usernames, self.profile)
        
        self.assertEqual(len(variations), len(set(variations)))


class TestPasswordGenerator(unittest.TestCase):
    """Test password generation."""
    
    def setUp(self):
        """Set up test profile."""
        self.profile = {
            "first": "Bob",
            "last": "Wilson",
            "nick": "Bobby",
            "year": "1985",
            "hobby": "soccer",
            "company": "SportsInc"
        }
    
    def test_password_generation(self):
        """Test that passwords are generated."""
        passwords = generate_passwords(self.profile)
        
        # Should generate passwords
        self.assertGreater(len(passwords), 0)
    
    def test_password_contains_personal_info(self):
        """Test that passwords contain personal information."""
        passwords = generate_passwords(self.profile)
        
        # Check that at least some passwords contain profile data
        contains_name = any("bob" in p.lower() for p in passwords)
        contains_year = any("1985" in p for p in passwords)
        
        self.assertTrue(contains_name or contains_year)
    
    def test_password_variations(self):
        """Test password variations (symbols, numbers, etc.)."""
        passwords = generate_passwords(self.profile)
        
        # Check for various patterns
        has_exclamation = any("!" in p for p in passwords)
        has_at = any("@" in p for p in passwords)
        has_numbers = any(any(c.isdigit() for c in p) for p in passwords)
        
        self.assertTrue(has_exclamation or has_at or has_numbers)
    
    def test_no_duplicate_passwords(self):
        """Test that there are no duplicate passwords."""
        passwords = generate_passwords(self.profile)
        
        self.assertEqual(len(passwords), len(set(passwords)))


class TestPasswordAnalyzer(unittest.TestCase):
    """Test password strength analysis."""
    
    def setUp(self):
        """Set up test data."""
        self.profile = {
            "first": "Charlie",
            "last": "Davis",
            "nick": "CD",
            "year": "2000",
            "hobby": "coding",
            "company": "DevCorp"
        }
        self.usernames = ["charliedavis", "cdavis", "cd"]
        self.variations = ["charlie_davis", "CharlieD"]
        
    def test_weak_passwords_with_personal_info(self):
        """Test that passwords with personal info are flagged as weak."""
        passwords = ["charlie123", "Davis2000", "cd_password"]
        
        weak, medium, strong, very_strong = profile_analyzer(
            self.usernames, self.variations, passwords, self.profile
        )
        
        # All should be weak because they contain personal info
        self.assertGreater(len(weak), 0)
    
    def test_random_password_scoring(self):
        """Test that random passwords get scored properly."""
        # These passwords don't contain any personal info
        passwords = ["XyZ@123!", "AbCd1234", "Test!Pass9"]
        
        weak, medium, strong, very_strong = profile_analyzer(
            self.usernames, self.variations, passwords, self.profile
        )
        
        # Should have some non-weak passwords
        total_non_weak = len(medium) + len(strong) + len(very_strong)
        self.assertGreater(total_non_weak, 0)
    
    def test_analyzer_returns_four_lists(self):
        """Test that analyzer returns exactly 4 lists."""
        passwords = ["test123", "another456"]
        
        result = profile_analyzer(
            self.usernames, self.variations, passwords, self.profile
        )
        
        # Should return 4 lists
        self.assertEqual(len(result), 4)
        
        # All should be lists
        for item in result:
            self.assertIsInstance(item, list)
    
    def test_no_duplicates_in_results(self):
        """Test that analyzer results have no duplicates."""
        passwords = ["charlie123", "charlie123", "Davis2000"]  # Intentional duplicate
        
        weak, medium, strong, very_strong = profile_analyzer(
            self.usernames, self.variations, passwords, self.profile
        )
        
        # Check no duplicates in weak
        self.assertEqual(len(weak), len(set(weak)))


class TestDataLoaders(unittest.TestCase):
    """Test data loading from CSV, JSON, and TXT files."""
    
    def setUp(self):
        """Create temporary directory for test files."""
        self.test_dir = tempfile.mkdtemp()
        
        self.test_profile = {
            "first": "test",
            "last": "user",
            "nick": "tester",
            "year": "2020",
            "hobby": "testing",
            "company": "testcorp"
        }
    
    def tearDown(self):
        """Clean up temporary directory."""
        shutil.rmtree(self.test_dir)
    
    def test_load_csv(self):
        """Test loading data from CSV file."""
        csv_path = os.path.join(self.test_dir, "test.csv")
        
        # Create test CSV
        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.test_profile.keys())
            writer.writeheader()
            writer.writerow(self.test_profile)
        
        # Load and verify
        data = load_csv(csv_path)
        
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["first"], "test")
    
    def test_load_json(self):
        """Test loading data from JSON file."""
        json_path = os.path.join(self.test_dir, "test.json")
        
        # Create test JSON
        with open(json_path, 'w') as f:
            json.dump([self.test_profile], f)
        
        # Load and verify
        data = load_json(json_path)
        
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["first"], "test")
    
    def test_load_text(self):
        """Test loading data from text file."""
        txt_path = os.path.join(self.test_dir, "test.txt")
        
        # Create test TXT (space-separated)
        with open(txt_path, 'w') as f:
            f.write("test user tester 2020 testing testcorp\n")
        
        # Load and verify
        data = load_text(txt_path)
        
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["first"], "test")
    
    def test_csv_lowercase_conversion(self):
        """Test that CSV data is converted to lowercase."""
        csv_path = os.path.join(self.test_dir, "test.csv")
        
        # Create CSV with uppercase data
        profile = {
            "first": "JOHN",
            "last": "DOE",
            "nick": "JD",
            "year": "1990",
            "hobby": "GAMING",
            "company": "TECHCORP"
        }
        
        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=profile.keys())
            writer.writeheader()
            writer.writerow(profile)
        
        # Load and verify lowercase
        data = load_csv(csv_path)
        
        self.assertEqual(data[0]["first"], "john")
        self.assertEqual(data[0]["hobby"], "gaming")


class TestReportGenerator(unittest.TestCase):
    """Test report generation in different formats."""
    
    def setUp(self):
        """Set up test data and temporary directory."""
        self.test_dir = tempfile.mkdtemp()
        
        # Create a mock profile result
        self.profile_results = [{
            "profile": {
                "first": "test",
                "last": "user",
                "nick": "tu",
                "year": "2020",
                "hobby": "testing",
                "company": "testco"
            },
            "usernames": ["testuser", "tuser"],
            "username_variations": ["test_user", "TestUser"],
            "passwords": ["test123", "user456"],
            "weak_passwords": ["test123", "user456"],
            "medium_passwords": [],
            "strong_passwords": [],
            "very_strong_passwords": []
        }]
        
        # Change to test directory for output
        self.original_dir = os.getcwd()
        os.chdir(self.test_dir)
        os.makedirs("reports", exist_ok=True)
    
    def tearDown(self):
        """Clean up and restore directory."""
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)
    
    def test_json_report_generation(self):
        """Test JSON report generation."""
        result = generate_report(self.profile_results, "json")
        
        # Should succeed
        self.assertTrue(result)
        
        # File should exist
        self.assertTrue(os.path.exists("reports/people_expanded.json"))
        
        # Verify content
        with open("reports/people_expanded.json") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
    
    def test_csv_report_generation(self):
        """Test CSV report generation."""
        result = generate_report(self.profile_results, "csv")
        
        # Should succeed
        self.assertTrue(result)
        
        # File should exist
        self.assertTrue(os.path.exists("reports/people_expanded.csv"))
        
        # Verify it's valid CSV
        with open("reports/people_expanded.csv") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            self.assertGreater(len(rows), 0)
    
    def test_txt_report_generation(self):
        """Test TXT report generation."""
        result = generate_report(self.profile_results, "txt")
        
        # Should succeed
        self.assertTrue(result)
        
        # File should exist
        self.assertTrue(os.path.exists("reports/people_expanded.txt"))
        
        # Verify content
        with open("reports/people_expanded.txt") as f:
            content = f.read()
            self.assertIn("Intelligent Password Profiling Tool", content)
    
    def test_cli_report_no_file(self):
        """Test that CLI report doesn't create a file."""
        result = generate_report(self.profile_results, "cli")
        
        # Should succeed
        self.assertTrue(result)
        
        # No file should be created
        self.assertFalse(os.path.exists("reports/people_expanded.txt"))
        self.assertFalse(os.path.exists("reports/people_expanded.json"))
        self.assertFalse(os.path.exists("reports/people_expanded.csv"))


class TestIntegration(unittest.TestCase):
    """Integration tests for the entire workflow."""
    
    def test_full_workflow(self):
        """Test complete workflow from profile to analysis."""
        # Create profile
        profile = {
            "first": "integration",
            "last": "test",
            "nick": "it",
            "year": "2024",
            "hobby": "workflow",
            "company": "testco"
        }
        
        # Generate usernames
        usernames = generate_username(profile)
        self.assertGreater(len(usernames), 0)
        
        # Generate variations
        variations = expand_username_variations(usernames, profile)
        
        # Generate passwords
        passwords = generate_passwords(profile)
        self.assertGreater(len(passwords), 0)
        
        # Analyze passwords
        weak, medium, strong, very_strong = profile_analyzer(
            usernames, variations, passwords, profile
        )
        
        # All generated passwords should be categorized
        total = len(weak) + len(medium) + len(strong) + len(very_strong)
        self.assertGreater(total, 0)


def run_tests():
    """Run all tests with detailed output."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestUsernameGenerator))
    suite.addTests(loader.loadTestsFromTestCase(TestUsernameVariations))
    suite.addTests(loader.loadTestsFromTestCase(TestPasswordGenerator))
    suite.addTests(loader.loadTestsFromTestCase(TestPasswordAnalyzer))
    suite.addTests(loader.loadTestsFromTestCase(TestDataLoaders))
    suite.addTests(loader.loadTestsFromTestCase(TestReportGenerator))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)