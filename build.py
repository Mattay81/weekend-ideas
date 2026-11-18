"""Copy ideas.csv into index.html so the page works on its own.

Run from this folder:  python3 build.py
It replaces everything between the CSV-START and CSV-END markers in index.html.
"""
import pathlib
import re

here = pathlib.Path(__file__).parent
csv_text = (here / "ideas.csv").read_text(encoding="utf-8-sig").strip()
if "</script" in csv_text.lower():
    raise SystemExit("ideas.csv contains '</script', which would break the page.")

page_path = here / "index.html"
page = page_path.read_text(encoding="utf-8")
new_page, count = re.subn(
    r"(<!-- CSV-START -->\n).*?(<!-- CSV-END -->)",
    lambda m: m.group(1) + csv_text + "\n" + m.group(2),
    page,
    flags=re.S,
)
if count != 1:
    raise SystemExit("Could not find the CSV markers in index.html.")
page_path.write_text(new_page, encoding="utf-8")
rows = csv_text.count("\n")
print(f"index.html rebuilt from ideas.csv (about {rows} ideas).")
