import copy


class Utils(object):

    matriz = []

    def criar(self, M, N):
        self.matriz = [[0]*N for i in range(M)]

    def limpar(self):
        try:
            self.matriz = [[0]*len(self.matriz[0])]*len(self.matriz)
        except IndexError:
            pass

    def desenhar_retangulo(self, linhas, colunas, x, y, cor):
        matriz = copy.deepcopy(self.matriz)
        try:
            if linhas > 0 and \
                                0 < colunas < len(self.matriz[0]) and \
                                x >= 0 and y >= 0:
                for i in range(linhas):
                    self.matriz[x+i][y:y+colunas] = [cor]*colunas
        except IndexError:
            self.matriz = matriz

    def preencher_regiao(self):
        pass

    def salvar(self, handle):
        handle.write(str(self))

    def __repr__(self):
        return "\n".join(
                            [
                                "".join(
                                            [str(pixel) for pixel in linha]
                                        )
                                for linha in self.matriz
                            ]
                        )
