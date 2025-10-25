# main.py
# Dual-mode entrypoint:
# 1) If there are CLI args -> keep the original single-dragon behavior.
# 2) If there are NO args   -> read the official task input from stdin (N lines).

import sys
import argparse

# ⬇️ This is the existing manager/builder module (kept as is).
#    It provides update_dragon_army_record(...) and display_strength()
from controller.DragonArmyManager import DragonArmyBuilder

# Defaults per task statement
DEFAULTS = {"damage": 45, "health": 250, "armor": 10}


def _parse_or_default(token: str, key: str) -> int:
    """
    Map 'null' -> default; otherwise int(). Important: '0' stays 0 (valid).
    """
    return DEFAULTS[key] if token.lower() == "null" else int(token)


# ---------- Official-task input reader (added) ----------
def _read_official_input():
    """
    Returns a list of (type, name, damage, health, armor) tuples.
    Works with both interactive runs (IntelliJ Run, terminal typing) and piped stdin.
    """
    items = []

    # If stdin is not a TTY, try to read the whole stream (e.g., tests/CI/heredoc)
    try:
        if not sys.stdin.isatty():
            buf = sys.stdin.read()
            if buf and buf.strip():
                lines = buf.strip().splitlines()
                n = int(lines[0].strip())
                i = 1
                for _ in range(n):
                    # skip any accidental empty lines
                    while i < len(lines) and not lines[i].strip():
                        i += 1
                    t, name, dmg, hp, ar = lines[i].split()
                    i += 1
                    d = _parse_or_default(dmg, "damage")
                    h = _parse_or_default(hp, "health")
                    a = _parse_or_default(ar, "armor")
                    items.append((t, name, d, h, a))
                return items
    except Exception:
        # fall back to interactive if something odd happened
        pass

    # Interactive fallback (TTY / IntelliJ console)
    try:
        n = int(input().strip())
    except EOFError:
        return items  # nothing to read
    for _ in range(n):
        line = input().strip()
        while not line:
            line = input().strip()
        t, name, dmg, hp, ar = line.split()
        d = _parse_or_default(dmg, "damage")
        h = _parse_or_default(hp, "health")
        a = _parse_or_default(ar, "armor")
        items.append((t, name, d, h, a))
    return items


def _run_from_stdin_with_model():
    """
    New path (added): read official input and feed the existing model.
    """
    entries = _read_official_input()
    if not entries:
        return

    army = DragonArmyBuilder()  # the existing manager

    for (t, name, d, h, a) in entries:
        # the existing API to insert/overwrite a dragon record
        army.update_dragon_army_record(t, name, d, h, a)

    # the existing display (note: prints in their current format)
    army.display_strength()


# ---------- The original single-dragon path (kept) ----------
def _run_from_args(argv):
    """
    This preserves the original behavior:
    one dragon per run via command-line args.
    """
    parser = argparse.ArgumentParser(
        description="Dragon Army — single-dragon updater (original flow)"
    )
    parser.add_argument("type", help="dragon type (e.g., Red, Black, Blue)")
    parser.add_argument("name", help="dragon name")
    # accept strings first so we can support 'null' like the task
    parser.add_argument("damage", help="damage or 'null'")
    parser.add_argument("health", help="health or 'null'")
    parser.add_argument("armor", help="armor or 'null'")

    args = parser.parse_args(argv)

    # Normalize 'null' here so the model always receives integers
    d = _parse_or_default(args.damage, "damage")
    h = _parse_or_default(args.health, "health")
    a = _parse_or_default(args.armor, "armor")

    army = DragonArmyBuilder()
    army.update_dragon_army_record(args.type, args.name, d, h, a)
    army.display_strength()


# ---------- Main ----------
def main():
    # If args present (beyond the script name), keep the original CLI flow.
    # Else, read official N-lines input from stdin.
    if len(sys.argv) > 1:
        # drop the script name and pass the rest to argparse
        _run_from_args(sys.argv[1:])
    else:
        _run_from_stdin_with_model()


if __name__ == "__main__":
    main()
