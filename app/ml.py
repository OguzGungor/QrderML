from .db import *

#collaborative mode
def testFunc(testparam):
    data = queryTest()
    print(data[0])
    return 3*testparam