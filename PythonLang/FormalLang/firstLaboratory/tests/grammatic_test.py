from unittest import TestCase, main
from PythonLang.FormalLang.firstLaboratory.main import main


class GrammaticTest(TestCase):
    def test_linear_right(self):
        self.assertEqual(main({'S': ['aS', 'aA'], 'A': ['bA', 'bZ'], 'Z': ['$']}), "Тип 3: регулярная правосторонняя грамматика")


    def test_linear_left(self):
        self.assertEqual(main({'S': ['Ab'], 'A': ['Ab', 'Za'], 'Z': ['Za', '$']}), "Тип 3: регулярная левосторонняя грамматика")


    def test_context_independent(self):
        self.assertEqual(main({'S': ['aSa', 'bSb', 'aa'], 'I': ['bb']}), "Тип 2: контекстно-свободная грамматика")


    def test_context_dependent(self):
        self.assertEqual(main({'S': ['aAS'], 'AS': ['AAS'], 'AAA': ['ABA'], 'A': ['b'], 'bBA': ['bcdA'], 'bS': ['ba']}), "Тип 1: контекстно-зависимая грамматика")

    def test_zero_type(self):
        self.assertEqual(main({'xAbCD': ['xHD']}), "Грамматика типа 0")