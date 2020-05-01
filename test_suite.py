from unittest import TestLoader, TestSuite, TextTestRunner
from login import Elearning_test1
from signup import Elearning_Test2
from logout import Elearning_test3
from do_test import Elearning_test4
from next_section import Elearning_test5


if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((

        loader.loadTestsFromTestCase(Elearning_test1),
        loader.loadTestsFromTestCase(Elearning_Test2),
        loader.loadTestsFromTestCase(Elearning_test3),
        loader.loadTestsFromTestCase(Elearning_test4),
        loader.loadTestsFromTestCase(Elearning_test5),



    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

