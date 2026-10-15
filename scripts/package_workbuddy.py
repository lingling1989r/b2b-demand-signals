"""Build a WorkBuddy ZIP with platform metadata; never includes research outputs or credentials."""
import argparse
from pathlib import Path
import zipfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--version', default='0.3.0')
parser.add_argument('--author', required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
source = (root / 'SKILL.md').read_text()
_, front, body = source.split('---', 2)
# Keep host-specific metadata in the distribution, preserving the portable source.
import json
fields = {
    'display_name': 'B端需求信号获客',
    'display_name_en': 'B2B Demand Signals',
    'description_zh': '多语言发现近期KOL、数据与B2B获客需求，按时间和ABC分级，交付原帖、账号、Excel底稿与回复草稿。需连接ClaudeBaby。',
    'description_en': 'Research recent multilingual B2B demand, prioritise fresh signals, and deliver source-linked Excel evidence and reply drafts. Requires ClaudeBaby.',
    'version': args.version,
    'author': args.author,
}
front += ''.join(f'{k}: {json.dumps(v, ensure_ascii=False)}\n' for k, v in fields.items())
args.output.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(args.output, 'w', zipfile.ZIP_DEFLATED) as archive:
    archive.writestr('b2b-demand-signals/SKILL.md', '---' + front + '---' + body)
    files = [root/'README.md', root/'scripts/grade_signals.py']
    for folder in ['references', 'examples', 'assets']:
        files += sorted((root/folder).glob('*'))
    for path in files:
        if path.is_file() and path.suffix in {'.md', '.json', '.py', '.png', '.xlsx'}:
            archive.write(path, 'b2b-demand-signals/' + path.relative_to(root).as_posix())
with zipfile.ZipFile(args.output) as archive:
    assert archive.testzip() is None
assert args.output.stat().st_size <= 3 * 1024 * 1024, 'WorkBuddy upload exceeds 3MB'
print(args.output)
