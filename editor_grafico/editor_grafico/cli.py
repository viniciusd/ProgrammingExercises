import cmd
from . import utils


class main(cmd.Cmd):

    prompt = ""

    def do_I(self, line):
        "Create a line matrix"
        line = line.split(" ")
        utils.create(line[0], line[1])

    def do_X(self, line):
        return True

    def do_EOF(self, line):
        return True

# def main():
#    while True:
#     cmds = input().split(" ")
#     print(cmds)
