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
                    do(self, line)
            return new_do
        return command

    @split_line(2)
    def do_I(self, line):
        try:
            self.utils.criar(int(line[0]), int(line[1]))
        except ValueError:
            pass

    @split_line(0)
    def do_C(self, line):
        self.utils.limpar()

    @split_line(3)
    def do_L(self, line):
        pass

    @split_line(4)
    def do_V(self, line):
        pass

    @split_line(4)
    def do_H(self, line):
        pass

    @split_line(5)
    def do_K(self, line):
        pass

    @split_line(3)
    def do_F(self, line):
        pass

    @split_line(1)
    def do_S(self, line):
        pass

    @split_line(0)
    def do_X(self, line):
        return True

    def do_EOF(self, line):
        return True

    def default(self, line):
        pass
