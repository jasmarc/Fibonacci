#!/usr/bin/env python
# encoding: utf-8
"""
fib.py

Created by Jason Marcell on 2009-07-13.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os

class Fibonacci:
	def gen(self, n):
         """Print a Fibonacci series up to n."""
         a, b = 0, 1
         while b < n:
             print b,
             a, b = b, a+b
