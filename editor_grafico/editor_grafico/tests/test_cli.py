#!/usr/local/bin/python3.4
import unittest
from unittest import mock
from editor_grafico import cli


patch = mock.patch


class TestCliCalls(unittest.TestCase):

    def set_up_split_line(self, arguments):
        self.do_mock, self.self_mock = mock.MagicMock(), mock.MagicMock()
        self.decorator = cli.Main.split_line(arguments)
        self.decorated = self.decorator(self.do_mock)

    def test_split_line_com_0_args_definidos_e_0_args_enviados(self):
        self.set_up_split_line(0)
        self.decorated(self.self_mock, "")
        self.assertTrue(self.do_mock.called)

    def test_split_line_com_0_args_definidos_e_1_arg_enviado(self):
        self.set_up_split_line(0)
        self.decorated(self.self_mock, "1")
        self.assertFalse(self.do_mock.called)

    def test_split_line_com_1_arg_definido_e_0_args_enviados(self):
        self.set_up_split_line(1)
        self.decorated(self.self_mock, "")
        self.assertFalse(self.do_mock.called)

    def test_split_line_com_1_arg_definido_e_1_arg_enviado(self):
        self.set_up_split_line(1)
        self.decorated(self.self_mock, "1")
        self.assertTrue(self.do_mock.called)

    def test_split_line_com_1_arg_definido_e_2_args_enviados(self):
        self.set_up_split_line(1)
        self.decorated(self.self_mock, "1 2")
        self.assertFalse(self.do_mock.called)

if __name__ == '__main__':
    unittest.main()
