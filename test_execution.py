'''TDD(Test-Driven Development)
unit-test for the program execution.py
Python version: 3.10
Author: Jeevitha Chandrappa'''

# using unittest module which is an in-built testing module
import unittest
import os
from execution import merge_csv

class TestExecution(unittest.TestCase):
    def setUp(self):
        # create temporary directory for testing
        self.test_dir = "test_dir"
        os.mkdir(self.test_dir)

        # creating sample csv files to run unit-tests
        header1 = ["ID","name", "age"]
        data1 = [["A1", "John", "30"], ["A2", "Mary", "25"], ["A3", "Bob", "35"], ["A4", "Lisa", "28"]]
        header2 = ["ID","Department","GPA"]
        data2 = [["A1", "Mathematics", "8.6"], ["A2", "CS", "8.2"], ["A3", "CS", "9.3"], ["A4", "CS", "7.5"]]
        self.file1 = os.path.join(self.test_dir, "small_file1.csv")
        self.file2 = os.path.join(self.test_dir, "small_file2.csv")
        with open(self.file1, "w") as f1:
            f1.write(",".join(header1) + "\n")
            for row in data1:
                f1.write(",".join(row) + "\n")
        with open(self.file2, "w") as f2:
            f2.write(",".join(header2) + "\n")
            for row in data2:
                f2.write(",".join(row) + "\n")

    def tearDown(self):
        # remove temporary directory and files
        try:
            os.remove(self.file1)
            os.remove(self.file2)
            os.rmdir(self.test_dir)
        except OSError:
            pass

    def test_execution(self):
        # test merging multiple CSV files
        file_names = os.listdir(os.path.abspath(self.test_dir))
        output_file = os.path.join(self.test_dir, "output_file.csv")
        merge_csv(file_names, os.path.abspath(self.test_dir))
        with open(output_file, "r") as f:
            lines = f.readlines()
        expected_lines = [
            "ID,name,age,Department,GPA\n",
            "A1,John,30,Mathematics,8.6\n",
            "A2,Mary,25,CS,8.2\n",
            "A3,Bob,35,CS,9.3\n",
            "A4,Lisa,28,CS,7.5\n"
        ]
        self.assertEqual(lines, expected_lines)

if __name__ == '__main__':
    unittest.main()
