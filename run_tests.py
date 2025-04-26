
import unittest
import sys

class CustomTestRunner(unittest.TextTestRunner):
    def run(self, test):
        result = super().run(test)
        if result.wasSuccessful():
            print("All test cases ran successfully")
        else:
            print("Some test cases failed")
        return result

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')
    runner = CustomTestRunner(verbosity=2)
    result = runner.run(test_suite)
    sys.exit(not result.wasSuccessful())
