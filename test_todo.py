"""Regression tests for the py-todo CLI (repo-root script `todo`).

Run with the standard library only: `python -m unittest test_todo -v`.
Each test runs the CLI in a subprocess with an isolated home directory so
the real ~/.config/py-todo and ~/.local/share/py-todo are never touched.
"""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TODO_SCRIPT = Path(__file__).with_name("todo")


def run_todo(*args, home):
    """Run the todo CLI with HOME/USERPROFILE pointed at an empty dir."""
    env = dict(os.environ)
    env["HOME"] = str(home)
    env["USERPROFILE"] = str(home)
    env["HOMEDRIVE"] = ""
    env["HOMEPATH"] = ""
    return subprocess.run(
        [sys.executable, str(TODO_SCRIPT), *args],
        capture_output=True,
        text=True,
        env=env,
    )


class TestTodoExitCodes(unittest.TestCase):
    def test_invalid_date_exits_nonzero(self):
        """An unparsable expiry date is an error: exit code must be nonzero."""
        with tempfile.TemporaryDirectory() as home:
            proc = run_todo("-a", "Write tests", "not-a-date", home=Path(home))
            self.assertIn(
                "An error occurred while parsing your date.", proc.stdout
            )
            self.assertNotEqual(
                proc.returncode,
                0,
                "invalid expiry date must not exit 0 (todo:parse_date_str)",
            )

    def test_invalid_date_adds_no_item(self):
        """The failed add must not leave an item behind."""
        with tempfile.TemporaryDirectory() as home:
            home = Path(home)
            run_todo("-a", "Write tests", "not-a-date", home=home)
            listed = run_todo("-l", home=home)
            self.assertIn("No items left on the reminder.", listed.stdout)

    def test_empty_date_add_is_accepted(self):
        """An empty expiry date means 'no expiry' and still exits 0."""
        with tempfile.TemporaryDirectory() as home:
            proc = run_todo("-a", "Write tests", "", home=Path(home))
            self.assertEqual(proc.returncode, 0)


if __name__ == "__main__":
    unittest.main()
