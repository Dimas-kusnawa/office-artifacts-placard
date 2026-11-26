"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum-placard line for an ordinary office object
(a lanyard) treated as an ancient artifact, in a deadpan curator voice,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

LINE = "Lanyard, c. 2019. Woven nylon, plastic clip. Worn at the throat to prove its bearer belonged to the tribe; the badge it carried was never once read. Donated by Human Resources."


def write_entry() -> None:
    """Write the placard line to entry.txt with no trailing newline."""
    import os

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    write_entry()
