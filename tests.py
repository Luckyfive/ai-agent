import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from functions.write_file import write_file


def run():
    print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum")')
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result1)

    print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result2)

    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result3)


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