#!/usr/local/bin/python3.4
import unittest
from unittest import mock
from editor_grafico import cli


patch = mock.patch


class TestCliCalls(unittest.TestCase):

    @patch('__main__.cli.main')
    def test_criar_matriz(self, mocked):
        assert True


if __name__ == '__main__':
    unittest.main()
