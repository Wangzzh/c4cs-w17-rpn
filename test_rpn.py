#! usr/bin/env python3

import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)

	def test_sub(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	
	def test_carat(self):
		result = rpn.calculate("2 3 ^")
		self.assertEqual(8, result)

	def test_carat2(self):
		result = rpn.calculate("3 2 1 ^ ^")
		self.assertEqaul(9, result)
