#!/usr/local/bin/python3.4
import unittest
from unittest import mock
from editor_grafico import cli, utils


patch = mock.patch


class TestUtils(unittest.TestCase):

    @staticmethod
    def matriz(M, N, val=0):
        return [[val]*N for i in range(M)]

    def setUp(self):
        self.utils = cli.utils.Utils()

    def test_criar_matriz_2x3(self):
        matriz_2x3 = self.matriz(2, 3)
        self.utils.criar(2, 3)
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_limpar_matriz_quando_vazia(self):
        self.utils.limpar()
        self.assertEqual(self.utils.matriz, [])

    def test_limpar_matriz_quando_matriz_2x3_de_1s(self):
        matriz_2x3 = self.matriz(2, 3)
        self.utils.matriz = self.matriz(2, 3, val=1)
        self.utils.limpar()
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_colorir_matriz_no_indice_1x1_quando_com_matriz_vazia(self):
        self.utils.colorir(1, 1, 'A')
        self.assertEqual(self.utils.matriz, [])

    def test_colorir_matriz_no_indice_1x1_quando_matriz_2x3(self):
        matriz_2x3 = self.matriz(2, 3)
        matriz_2x3[1][1] = 'A'
        self.utils.matriz = self.matriz(2, 3)
        self.utils.colorir(1, 1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_desenhar_retangulo_1x2_no_idice_0x1_quando_com_matriz_vazia(self):
        """ Esse caso cobre os casos em que teríamos IndexError """
        self.utils.desenhar_retangulo(1, 2, 0, 1, 'A')
        self.assertEqual(self.utils.matriz, [])

    def test_desenhar_retangulo_1x2_no_idice_0x1_quando_matriz_2x3(self):
        matriz_2x3 = self.matriz(2, 3)
        matriz_2x3[0][1:3] = ['A']*2
        self.utils.matriz = self.matriz(2, 3)
        self.utils.desenhar_retangulo(1, 2, 0, 1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_desenhar_retangulo_2x1_no_idice_0x1_quando_matriz_2x3(self):
        matriz_2x3 = self.matriz(2, 3)
        matriz_2x3[0][1], matriz_2x3[1][1] = 'A', 'A'
        self.utils.matriz = self.matriz(2, 3)
        self.utils.desenhar_retangulo(2, 1, 0, 1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_desenhar_retangulo_2x2_no_idice_0x1_quando_matriz_2x3(self):
        matriz_2x3 = self.matriz(2, 3)
        matriz_2x3[0][1:3], matriz_2x3[1][1:3] = ['A']*2, ['A']*2
        self.utils.matriz = self.matriz(2, 3)
        self.utils.desenhar_retangulo(2, 2, 0, 1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_desenhar_retangulo_quando_retngulo_sai_da_matriz_pelas_cols(self):
        matriz_2x3 = self.matriz(2, 3)
        self.utils.matriz = self.matriz(2, 3)
        self.utils.desenhar_retangulo(2, 4, 0, 1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_desenhar_retngulo_quando_retngulo_sai_da_matriz_pelas_linhs(self):
        matriz_2x3 = self.matriz(2, 3)
        self.utils.matriz = self.matriz(2, 3)
        self.utils.desenhar_retangulo(4, 2, 0, 1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_desenhar_retangulo_quando_linhas_é_negativo(self):
        matriz_2x3 = self.matriz(2, 3)
        self.utils.matriz = self.matriz(2, 3)
        self.utils.desenhar_retangulo(-3, 2, 0, 1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_desenhar_retangulo_quando_colunas_é_negativo(self):
        matriz_2x3 = self.matriz(2, 3)
        self.utils.matriz = self.matriz(2, 3)
        self.utils.desenhar_retangulo(1, -2, 0, 1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_desenhar_retangulo_quando_x_é_negativo(self):
        matriz_2x3 = self.matriz(2, 3)
        self.utils.matriz = self.matriz(2, 3)
        self.utils.desenhar_retangulo(1, 2, -4, 1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

    def test_desenhar_retangulo_quando_y_é_negativo(self):
        matriz_2x3 = self.matriz(2, 3)
        self.utils.matriz = self.matriz(2, 3)
        self.utils.desenhar_retangulo(1, 2, 0, -1, 'A')
        self.assertEqual(self.utils.matriz, matriz_2x3)

if __name__ == '__main__':
    unittest.main()
