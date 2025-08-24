import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.working_directory = "calculator"

    def test_get_files_info(self):
        print("\nget_files_info(\"calculator\", \".\"):")
        print("Result for current directory:")
        files_info = get_files_info("calculator", ".")
        print(files_info)
        
        self.assertIsInstance(files_info, str)
        self.assertTrue(len(files_info) > 0)
        # Check that it contains expected files
        self.assertIn("main.py", files_info)
        self.assertIn("pkg", files_info)
        self.assertIn("tests.py", files_info)

    def test_get_files_info_with_subdirectory(self):
        print("\nget_files_info(\"calculator\", \"pkg\"):")
        print("Result for 'pkg' directory:")
        files_info = get_files_info("calculator", "pkg")
        print(files_info)
        
        self.assertIsInstance(files_info, str)
        self.assertTrue(len(files_info) > 0)
        # Check that it contains expected files
        self.assertIn("calculator.py", files_info)
        self.assertIn("render.py", files_info)

    def test_invalid_directory(self):
        print("\nget_files_info(\"calculator\", \"invalid_dir\"):")
        print("Result for 'invalid_dir' directory:")
        files_info = get_files_info("calculator", "invalid_dir")
        print(f"    {files_info}")
        
        self.assertIsInstance(files_info, str)
        self.assertTrue(files_info.startswith("Error:"))

    def test_outside_working_directory_absolute_path(self):
        print("\nget_files_info(\"calculator\", \"/bin\"):")
        print("Result for '/bin' directory:")
        files_info = get_files_info("calculator", "/bin")
        print(f"    {files_info}")
        
        self.assertIsInstance(files_info, str)
        self.assertTrue(files_info.startswith("Error:"))
        self.assertIn("outside the permitted working directory", files_info)

    def test_outside_working_directory_relative_path(self):
        print("\nget_files_info(\"calculator\", \"../\"):")
        print("Result for '../' directory:")
        files_info = get_files_info("calculator", "../")
        print(f"    {files_info}")
        
        self.assertIsInstance(files_info, str)
        self.assertTrue(files_info.startswith("Error:"))
        self.assertIn("outside the permitted working directory", files_info)

if __name__ == "__main__":
    unittest.main()