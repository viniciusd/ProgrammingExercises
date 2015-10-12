import os
import importlib
import io
import editor_grafico
import builtins
import unittest
import pep8
import inspect
from unittest import mock


patch = mock.patch


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


class TestIntegration(unittest.TestCase):

    saved_files = dict()

    class MockedCli(editor_grafico.cli.Main):

        def __init__(self, id, saved_files):
            self.id = id 
            self.saved_files = saved_files

        @staticmethod
        def mocked_open():
            def io_side_effect(file_name):
                self = inspect.stack()[3][0].f_locals["self"]
                try:
                    self.saved_files[self.id] = {**self.saved_files[self.id], file_name : None}
                except KeyError:
                    self.saved_files[self.id] = {file_name : None}
                return mock.DEFAULT
            mocked = mock.Mock()
            mocked.return_value = io.StringIO()
            mocked.return_value.close = lambda: None
            mocked.side_effect = io_side_effect
            return mocked

        def do_S(self, *args, **kwargs):
            builtins.open = self.mocked_open()
            exit = super().do_S(*args, **kwargs )
            for fname in self.saved_files[self.id]:
                if not self.saved_files[self.id][fname]:
                    self.saved_files[self.id][fname] = builtins.open.return_value.getvalue()
                    break
            importlib.reload(builtins)
            return exit

    def setUp(self):
        self.test_cli = self.MockedCli(self.id(), self.saved_files)

    def tearDown(self):
        del self.saved_files[self.id()]

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

        one = self.test_cli.saved_files[self.id()]['one.bmp']
        two = self.test_cli.saved_files[self.id()]['two.bmp']
        
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
        importlib.reload(builtins)

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

        one = self.test_cli.saved_files[self.id()]['one.bmp']

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
