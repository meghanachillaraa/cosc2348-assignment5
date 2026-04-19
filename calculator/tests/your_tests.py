#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Checks taht the program outputs "7" for an input of "10 - 3"
assert run("10 - 3").output == "7"
# Checks that the program outputs "5" for an input of "20 / 4"
assert run("20 / 4").output == "5"

###

print("All tests passed!")
