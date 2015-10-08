import os
import editor_grafico
import unittest
import pep8


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        path = os.path.dirname(editor_grafico.__file__)
        f = []
        for (dirpath, dirnames, filenames) in os.walk(path):
            f.extend([
                        dirpath+'/'+filename for filename in filenames
                        if len(filename) > 3 and filename[-3:] == ".py"
                     ]
                     )
        pep8style = pep8.StyleGuide(quit=True)
        result = pep8style.check_files(f)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestSystem(unittest.TestCase):

    def setUp(self):
        self.test_cli = editor_grafico.cli.main()

    # TODO: Mock the files
    def test_entrada_01(self):
        self.test_cli.onecmd('I 5 6')
        self.test_cli.onecmd('L 2 3 A')
        self.test_cli.onecmd('S one.bmp')
        self.test_cli.onecmd('G 2 3 J')
        self.test_cli.onecmd('V 2 3 4 W')
        self.test_cli.onecmd('H 3 4 2 Z')
        self.test_cli.onecmd('F 3 3 J')
        self.test_cli.onecmd('S two.bmp')
        self.test_cli.onecmd('X')

        with open('one.bmp') as f:
            one = f.read()

        with open('two.bmp') as f:
            two = f.read()

        self.assertEqual(one, (
                                "00000\n"
                                "00000\n"
                                "0A000\n"
                                "00000\n"
                                "00000\n"
                                "00000\n"
                                )
                         )
        self.assertEqual(two, (
                                "JJJJJ\n"
                                "JJZZJ\n"
                                "JWJJJ\n"
                                "JWJJJ\n"
                                "JJJJJ\n"
                                "JJJJJ\n"
                                )
                         )

    # TODO: Mock the files
    def test_entrada_02(self):
        self.test_cli.onecmd('I 10 9')
        self.test_cli.onecmd('L 5 3 A')
        self.test_cli.onecmd('G 2 3 J')
        self.test_cli.onecmd('V 2 3 4 W')
        self.test_cli.onecmd('H 1 10 5 Z')
        self.test_cli.onecmd('F 3 3 J')
        self.test_cli.onecmd('K 2 7 8 8 E')
        self.test_cli.onecmd('F 9 9 R')
        self.test_cli.onecmd('S one.bmp')
        self.test_cli.onecmd('X')

        with open('one.bmp') as f:
            one = f.read()

        self.assertEqual(one, (
                                "JJJJJJJJJJ\n"
                                "JJJJJJJJJJ\n"
                                "JWJJAJJJJJ\n"
                                "JWJJJJJJJJ\n"
                                "ZZZZZZZZZZ\n"
                                "RRRRRRRRRR\n"
                                "REEEEEEERR\n"
                                "REEEEEEERR\n"
                                "RRRRRRRRRR\n"
                                )
                         )
if __name__ == '__main__':
    unittest.main()
