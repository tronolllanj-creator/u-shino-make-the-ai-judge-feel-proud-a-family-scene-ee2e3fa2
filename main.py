import os
import sys
from pathlib import Path


SCENE = "Crooked family drawing -- Dad hangs it level, then tilts his head in every photo to match it. Mom's fridge magnet collection finally makes sense."


def main() -> int:
    """Write a warm, funny family scene to $MAKEFUN_OUTPUT_DIR/entry.txt."""
# Entry validated: output is 1-280 chars, one or two lines, deterministic.
    output_dir = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', 'out'))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / 'entry.txt'

    content = SCENE + '\n'

    if not (1 <= len(content) <= 280 and content.strip() and 1 <= content.count(chr(10)) <= 2):
        raise ValueError('Content validation failed')

    output_path.write_text(content, encoding='utf-8')
    print(f'{output_path} {len(content)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
