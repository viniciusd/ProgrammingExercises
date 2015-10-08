import cmd
from . import utils


class main(cmd.Cmd):

    prompt = ""
    utils = utils.Utils

    def do_I(self, line):
        "Create a matrix"
        line = line.split(" ")
        self.utils.criar(line[0], line[1])

    def do_C(self, line):
        pass

    def do_L(self, line):
        pass

    def do_V(self, line):
        pass

    def do_H(self, line):
        pass

    def do_K(self, line):
        pass

    def do_F(self, line):
        pass

    def do_S(self, line):
        pass

    def do_X(self, line):
        return True

    def do_EOF(self, line):
        return True

    def default(self, line):
        pass

# def main():
#    while True:
#     cmds = input().split(" ")
#     print(cmds)
