"""Write one short out-of-office auto-reply for a make.fun bounty."""

import os
import sys
from pathlib import Path

TEXT = (
    "On leave until the 14th. A wasp has built a nest in the mailbox and I respect "
    "her. All my mail is being held at the post office, and by the wasp."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text must be 1-280 characters, got {len(TEXT)}"
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
