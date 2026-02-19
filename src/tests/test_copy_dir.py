import tempfile
import unittest
from pathlib import Path

from functions.copy_dir import copy_dir


class TestCopyDir(unittest.TestCase):
    def test_copy_dir_copies_nested_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "source"
            dest = tmp_path / "dest"

            (source / "nested").mkdir(parents=True)
            (source / "root.txt").write_text("root", encoding="utf-8")
            (source / "nested" / "child.txt").write_text("child", encoding="utf-8")

            copy_dir(str(source), str(dest))

            self.assertEqual((dest / "root.txt").read_text(encoding="utf-8"), "root")
            self.assertEqual((dest / "nested" / "child.txt").read_text(encoding="utf-8"), "child")

    def test_copy_dir_writes_log_when_log_path_provided(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "source"
            dest = tmp_path / "dest"
            log_file = tmp_path / "copy.log"

            source.mkdir(parents=True)
            (source / "one.txt").write_text("1", encoding="utf-8")
            (source / "two.txt").write_text("2", encoding="utf-8")

            copy_dir(str(source), str(dest), str(log_file))

            self.assertTrue(log_file.exists())
            log_lines = log_file.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(log_lines), 2)
            for line in log_lines:
                self.assertTrue(line.startswith("COPIED "))
                self.assertIn(" -> ", line)


if __name__ == "__main__":
    unittest.main()
