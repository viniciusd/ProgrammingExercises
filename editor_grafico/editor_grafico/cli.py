import cmd
from . import utils


class Main(cmd.Cmd):

    prompt = ""
    utils = utils.Utils()

    def split_line(arguments):
        def command(do):
            def new_do(self, line):
                line = line.split()
                if len(line) == arguments:
                    return do(self, line)
                return False
            return new_do
        return command

    @split_line(2)
    def do_I(self, line):
        try:
            self.utils.criar(int(line[0]), int(line[1]))
        except ValueError:
            pass
        return False

    @split_line(0)
    def do_C(self, line):
        self.utils.limpar()
        return False

    @split_line(3)
    def do_L(self, line):
        try:
            self.utils.desenhar_retangulo(
                                            1,
                                            1,
                                            int(line[0]),
                                            int(line[1]),
                                            line[2]
                                          )
        except ValueError:
            pass
        return False

    @split_line(4)
    def do_V(self, line):
        try:
            x, y1, y2, c = int(line[0]), int(line[1]), int(line[2]), line[3]
            self.utils.desenhar_retangulo(
                                            y2-y1+1,
                                            1,
                                            x,
                                            y1,
                                            c
                                          )
        except ValueError:
            pass
        return False

    @split_line(4)
    def do_H(self, line):
        try:
            x1, x2, y, c = int(line[0]), int(line[1]), int(line[2]), line[3]
            self.utils.desenhar_retangulo(
                                            1,
                                            x2-x1+1,
                                            x1,
                                            y,
                                            c
                                          )
        except ValueError:
            pass
        return False

    @split_line(5)
    def do_K(self, line):
        try:
            x1, y1 = int(line[0]), int(line[1])
            x2, y2 = int(line[2]), int(line[3])
            c = line[4]
            self.utils.desenhar_retangulo(
                                            x2-x1+1,
                                            y2-y1+1,
                                            x1,
                                            y1,
                                            c
                                          )
        except ValueError:
            pass
        return False

    @split_line(3)
    def do_F(self, line):
        pass

    @split_line(1)
    def do_S(self, line):
        with open(line[0]) as output_handle:
            self.utils.salvar(output_handle)
        return False

    @split_line(0)
    def do_X(self, line):
        return True

    def do_EOF(self, line):
        return True

    def default(self, line):
        return False
