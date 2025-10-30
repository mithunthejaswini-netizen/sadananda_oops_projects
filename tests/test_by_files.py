import pathlib
import subprocess
import sys
import difflib
import pytest

CASES_DIR = pathlib.Path(__file__).parent / "cases"
PROJECT_ROOT = CASES_DIR.parent.parent  # where main.py lives


def _norm(s: str) -> str:
    return "\n".join(line.rstrip() for line in s.strip().splitlines())


def _run_case(in_path: pathlib.Path) -> str:
    proc = subprocess.run(
        [sys.executable, "main.py"],
        cwd=str(PROJECT_ROOT),
        input=in_path.read_text(encoding="utf-8").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=10,
    )
    if proc.returncode != 0:
        raise AssertionError(
            f"Process exited {proc.returncode}:\n{proc.stderr.decode('utf-8', 'ignore')}"
        )
    return proc.stdout.decode("utf-8")


def _first_diff(a: str, b: str) -> str | None:
    a_lines = a.splitlines()
    b_lines = b.splitlines()
    for i, (la, lb) in enumerate(zip(a_lines, b_lines), start=1):
        if la != lb:
            return f"First difference at line {i}:\n  ACTUAL : {la}\n  EXPECT : {lb}"
    if len(a_lines) != len(b_lines):
        return f"Different number of lines: actual={len(a_lines)}, expected={len(b_lines)}"
    return None


_CASES = sorted(CASES_DIR.glob("*.in"))
IDS = [p.stem for p in _CASES]


@pytest.mark.parametrize("in_path", _CASES, ids=IDS)
def test_case(in_path):
    out_path = in_path.with_suffix(".out")
    assert out_path.exists(), f"Missing expected file for {in_path.name}"

    actual = _norm(_run_case(in_path))
    expected = _norm(out_path.read_text(encoding="utf-8"))

    passed = (actual == expected)
    case_name = in_path.stem
    status = "PASS" if passed else "FAIL"
    print(f"[{case_name}] — {status}")

    if not passed:
        reason = _first_diff(actual, expected)
        if reason:
            print(reason)

        diff = "\n".join(
            difflib.unified_diff(
                expected.splitlines(),
                actual.splitlines(),
                fromfile=f"{case_name}.out (expected)",
                tofile=f"{case_name}.actual (actual)",
                lineterm="",
                n=3,
            )
        )
        if diff:
            print("\n--- unified diff ---")
            print(diff)

        # <-- This line makes the summary include the reason
        pytest.fail(f"Case: {case_name}\n{reason or 'Mismatch'}\nSee unified diff above.", pytrace=False)
