#!/usr/local/bin/python3.4
import unittest
from unittest import mock
from editor_grafico import cli
import builtins
import importlib
import io

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

    def test_do_I_quando_com_sintaxe_correta(self):
        test_cli = cli.Main()
        test_cli.utils.criar = mock.MagicMock()
        test_cli.onecmd('I 1 2')
        self.assertTrue(test_cli.utils.criar.called)

    def test_do_I_quando_com_m_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.criar = mock.MagicMock()
        test_cli.onecmd('I A 2')
        self.assertFalse(test_cli.utils.criar.called)

    def test_do_I_quando_com_n_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.criar = mock.MagicMock()
        test_cli.onecmd('I 1 A')
        self.assertFalse(test_cli.utils.criar.called)

    def test_do_C(self):
        test_cli = cli.Main()
        test_cli.utils.limpar = mock.MagicMock()
        test_cli.onecmd('C')
        self.assertTrue(test_cli.utils.limpar.called)

    def test_do_L_quando_com_sintaxe_correta(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('L 1 2 A')
        test_cli.utils.desenhar_retangulo.assert_called_with(1, 1, 1, 2, 'A')

    def test_do_L_quando_com_x_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('L A 2 A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_L_quando_com_y_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('L 1 A A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_V_quando_com_sintaxe_correta(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('V 1 2 3 A')
        test_cli.utils.desenhar_retangulo.assert_called_with(2, 1, 1, 2, 'A')

    def test_do_V_quando_com_x_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('V A 2 3 A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_V_quando_com_y1_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('V 1 A 3 A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_V_quando_com_y2_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('V 1 2 A A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_H_quando_com_sintaxe_correta(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('H 1 2 3 A')
        test_cli.utils.desenhar_retangulo.assert_called_with(1, 2, 1, 3, 'A')

    def test_do_H_quando_com_x1_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('H A 2 3 A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_H_quando_com_x2_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('H 1 A 3 A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_H_quando_com_y_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('H 1 2 A A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_K_quando_com_sintaxe_correta(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('K 0 0 1 2 A')
        test_cli.utils.desenhar_retangulo.assert_called_with(2, 3, 0, 0, 'A')

    def test_do_K_quando_com_x1_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('K A 0 1 2 A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_K_quando_com_x2_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('K 0 0 A 2 A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_K_quando_com_y1_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('K 0 A 1 2 A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_K_quando_com_y2_nao_numerico(self):
        test_cli = cli.Main()
        test_cli.utils.desenhar_retangulo = mock.MagicMock()
        test_cli.onecmd('K 0 0 1 A A')
        self.assertFalse(test_cli.utils.desenhar_retangulo.called)

    def test_do_S(self):
        builtins.open = mock.Mock()
        builtins.open.return_value = io.StringIO()
        test_cli = cli.Main()
        test_cli.utils.salvar = mock.MagicMock()
        test_cli.onecmd('S one.bmp')
        self.assertTrue(test_cli.utils.salvar.called)
        importlib.reload(builtins)

    def test_do_X(self):
        test_cli = cli.Main()
        self.assertTrue(test_cli.onecmd('X'))

if __name__ == '__main__':
    unittest.main()
