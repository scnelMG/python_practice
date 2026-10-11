"""Reject Riot API key literals in tracked files without printing their values."""

from pathlib import Path
import re
import subprocess


KEY_PATTERN = re.compile(rb"RGAPI-[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}")


def exposed_files(root):
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True
    )
    paths = [name.decode("utf-8") for name in result.stdout.split(b"\0") if name]
    return [name for name in paths if KEY_PATTERN.search((root / name).read_bytes())]


def main():
    try:
        hits = exposed_files(Path(__file__).resolve().parents[1])
    except (OSError, subprocess.CalledProcessError, UnicodeError):
        print("FAIL: could not scan every tracked file.")
        return 1
    for name in hits:
        print(f"FAIL: Riot API key literal found in {name}")
    if not hits:
        print("PASS: no Riot API key literals in tracked files.")
    return int(bool(hits))


if __name__ == "__main__":
    raise SystemExit(main())
