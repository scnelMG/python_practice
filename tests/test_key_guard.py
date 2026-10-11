from pathlib import Path
import subprocess
import tempfile
import unittest
import uuid

from scripts.check_riot_keys import exposed_files


class KeyGuardTests(unittest.TestCase):
    def test_scans_unicode_paths_and_notebook_outputs_without_leaking_values(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            fake_key = "RGAPI-" + str(uuid.UUID(int=0))
            (root / "한글 노트북.ipynb").write_text(
                '{"outputs": ["' + fake_key + '"]}', encoding="utf-8"
            )
            (root / "safe.py").write_text('api_key = os.environ["RIOT_API_KEY"]')
            subprocess.run(["git", "add", "--", "."], cwd=root, check=True)
            self.assertEqual(exposed_files(root), ["한글 노트북.ipynb"])
            (root / "한글 노트북.ipynb").write_text('{"outputs": []}')
            self.assertEqual(exposed_files(root), [])

    def test_git_failure_is_not_reported_as_a_clean_scan(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(subprocess.CalledProcessError):
                exposed_files(Path(directory))


if __name__ == "__main__":
    unittest.main()
