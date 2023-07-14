import unittest

# from typing import Tuple, List, Callable, Union, TypeVar, Optional
# from functools import reduce


from Lexer.tokens import *
from Lexer.lexer import *
from Runner.runner import *
from Parser.parser import *
from Tools.tools import *




# class Test_tokens(unittest.TestCase):
#     def TestDirectoryToken(self):
#         self.assertEqual(Directory("test"), "Handles looping, conditionals and code separation")
    


# test = dif_("test",1)

# match test:
#     case dif_():
#         print("test")
#     case _:
#         print("fail")

from UnitTests.unitTestRunner import *


if __name__ == '__main__':
    unittest.main()