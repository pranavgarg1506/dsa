"""
Need to REVISIT AGAIN
"""

import sys 
import os
from dotenv import load_dotenv
load_dotenv()

BASE_PATH = os.getenv('BASE_PATH')
CUR_PATH = BASE_PATH + '/ds'

sys.path.insert(0, CUR_PATH)

from stack import StackUsingList

"""
Algorithm:-

1. reverse the infix the expression
2. Obtain postfix expression of the modified expression.
3. reverse the output obtained from the above expression.

"""



expression = "x+y*z/w+u"

