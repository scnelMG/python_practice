from pathlib import Path
import subprocess
import sys
import tokenize
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ArchiveTests(unittest.TestCase):
    def test_tracked_python_files_parse(self):
        paths = subprocess.check_output(
            ['git', 'ls-files', '-z', '--', '*.py'], cwd=ROOT
        ).decode('utf-8').split('\0')
        for name in filter(None, paths):
            with self.subTest(path=name):
                with tokenize.open(ROOT / name) as source:
                    compile(source.read(), name, 'exec')

    def test_prime_exercise_handles_small_numbers_and_odd_composites(self):
        for bound, expected in [(1, []), (2, [2]), (25, [2, 3, 5, 7, 11, 13, 17, 19, 23])]:
            with self.subTest(bound=bound):
                result = subprocess.run(
                    [sys.executable, str(ROOT / 'homework_help/untitled1.py')],
                    input=str(bound), text=True, capture_output=True, check=True,
                )
                self.assertEqual([int(n) for n in result.stdout.split()], expected)
