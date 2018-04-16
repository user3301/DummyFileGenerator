# -*- coding: utf-8 -*-

from lib.core import*

import unittest




class LibTestSuite(unittest.TestCase):
    """lib test cases."""

    def test_generate_file_name(self):
        value = generateFileName()
        self.assertEqual("dummy_file_%(time)s.mp3"%{"time":time.strftime("%Y%m%d%H%M%S", time.localtime())}, value)

    def test_create_file(self):
        createFile(outputDir)

if __name__ == '__main__':
    unittest.main()