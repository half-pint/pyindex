#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Some tests for pyindex (currently just very basic tests for interleave.py)"""

import unittest
import interleave

class TestInterleave(unittest.TestCase):

    def test_interleave2(self):
        self.assertEqual(hex(interleave.interleave2(0x00, 0xFF)), hex(43690))
        self.assertEqual(hex(interleave.interleave2(0x0000, 0xFFFF)), hex(2863311530))

    def test_interleave3(self):
        self.assertEqual(hex(interleave.interleave3(0x00, 0xFF, 0x00)), hex(4793490))
        self.assertEqual(hex(interleave.interleave3(0x0000, 0xFFFF, 0x0000)), hex(306783378))

    def test_interleave4(self):
        self.assertEqual(hex(interleave.interleave4(0x00, 0xFF, 0x00, 0xFF)), hex(2863311530))

    def test_idempotency(self):
        integers = (4, 42)
        interleaved = interleave.interleave2(*integers)
        self.assertEqual(integers, interleave.deinterleave2(interleaved))

if __name__ == '__main__':
    unittest.main()
