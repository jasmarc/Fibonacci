#!/usr/bin/env python
# encoding: utf-8
"""
test_fib.py

Created by Jason Marcell on 2009-07-14.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import unittest
from fib import Fibonacci

class TestFib(unittest.TestCase):
    def setUp(self):
        pass

    def test_fib(self):
        self.fib = Fibonacci()
        self.fib.gen(5)
    
if __name__ == '__main__':
    unittest.main()