import sys 
import os
from dotenv import load_dotenv
load_dotenv()

BASE_PATH = os.getenv('BASE_PATH')
CUR_PATH = BASE_PATH + '/ds'

sys.path.insert(0, CUR_PATH)

from stack import StackUsingList

_map = {
    ']' : '[',
    '}' : '{',
    ')' : '('
}

expression = '()[{[()()]}]'
s = StackUsingList()
tillBalanced = True

for char in expression:

    if char in ["(", "{", "["]:
        s.push(char)

    else:
        
        ## 1. stack should not be empty
        if s.isEmpty():
            tillBalanced = False
            break

        ## 2. matching the bracket pair
        brack = _map[char]
        if brack != s.pop():
            tillBalanced = False
            break
        


if tillBalanced:
    print(True)
else:
    print(False)


