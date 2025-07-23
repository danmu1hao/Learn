import os
import sys
path=os.path.join(os.path.dirname(__file__),'..')
PROJECT_ROOT = os.path.abspath(
    path 
)
sys.path.append(PROJECT_ROOT)
print(path)
print(PROJECT_ROOT)

from sub import sub_py 
sub_py.Test2

import sub2.sub2_py as sub2
sub2.Test()

from sub.sub_sub.sub_sub_py import Test as T
T()
from sub2.sub.sub.test import Test as Test2
Test2()