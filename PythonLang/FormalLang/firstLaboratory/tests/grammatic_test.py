from unittest import TestCase, main
from PythonLang.FormalLang.firstLaboratory.main import main


class GrammaticTest(TestCase):
    def test_linear_left(self):
        self.assertEqual(main())