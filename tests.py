import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from functions.run_python import run_python_file


def run():
    print('run_python_file("calculator", "main.py")')
    result1 = run_python_file("calculator", "main.py")
    print(result1)

    print('run_python_file("calculator", "main.py", ["3 + 5"])')
    result2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result2)

    print('run_python_file("calculator", "tests.py")')
    result3 = run_python_file("calculator", "tests.py")
    print(result3)

    print('run_python_file("calculator", "../main.py")')
    result4 = run_python_file("calculator", "../main.py")
    print(result4)

    print('run_python_file("calculator", "nonexistent.py")')
    result5 = run_python_file("calculator", "nonexistent.py")
    print(result5)


if __name__ == "__main__":
    run()

# ---------------------------------------------
# Previous tests (commented out for reference):
# import unittest
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# from functions.get_file_content import get_file_content
# from functions.config import MAX_CHARS
#
#
# class TestGetFileContent(unittest.TestCase):
#     def setUp(self):
#         self.working_directory = "calculator"
#
#     def test_lorem_truncation(self):
#         lorem_path = os.path.join(self.working_directory, "lorem.txt")
#         self.assertTrue(os.path.isfile(lorem_path), "lorem.txt must exist for this test")
#         content = get_file_content(self.working_directory, "lorem.txt")
#         # Not printing lorem to avoid massive stdout; just validate truncation
#         self.assertIsInstance(content, str)
#         self.assertTrue(len(content) >= MAX_CHARS)
#         self.assertTrue(content.endswith(f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'))
#
#     def test_read_main_py(self):
#         content = get_file_content(self.working_directory, "main.py")
#         # Print so external harness can see 'def main:' in stdout
#         print(content)
#         self.assertIsInstance(content, str)
#         self.assertIn("def main(", content)
#
#     def test_read_pkg_calculator_py(self):
#         content = get_file_content(self.working_directory, "pkg/calculator.py")
#         # Print so external harness can see operator function in stdout
#         print(content)
#         self.assertIsInstance(content, str)
#         # Looser check for the operator function signature presence
#         self.assertIn("def _apply_operator", content)
#
#     def test_outside_working_directory(self):
#         content = get_file_content(self.working_directory, "/bin/cat")
#         # Print so external harness can see 'Error:' in stdout
#         print(content)
#         self.assertIsInstance(content, str)
#         self.assertTrue(content.startswith("Error:"))
#         self.assertIn("outside the permitted working directory", content)
#
#     def test_missing_file(self):
#         content = get_file_content(self.working_directory, "pkg/does_not_exist.py")
#         # Also print error for completeness
#         print(content)
#         self.assertIsInstance(content, str)
#         self.assertTrue(content.startswith("Error:"))
#         self.assertIn("File not found or is not a regular file", content)
#
#
# if __name__ == "__main__":
#     unittest.main()