import argparse
import black

from pathlib import Path

# Parse command line args
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

from jinja2 import Template

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--year", type=int, help="Year of AoC to create")
parser.add_argument(
    "-d",
    "--directory",
    type=str,
    help="Working directory to scaffold project in",
    default=".",
)

args = parser.parse_args()
if not args.year:
    raise AttributeError("Missing year argument")

env = Environment(loader=FileSystemLoader("templates"))

# Create root folder
wd = Path(args.directory).resolve()
root = wd / f"aoc_{args.year}"
root.mkdir(exist_ok=True)

# Create each day
test_tmp = env.get_template("tests.py.jinja")
init_tmp = env.get_template("__init__.py.jinja")

for day in range(1, 26):
    d = f"{day:02d}"
    tmp_args = {"day": d, "year": args.year}

    folder = root / f"day_{d}"
    folder.mkdir(exist_ok=True)

    # input.txt
    (folder / "inputs.txt").touch(exist_ok=True)

    # tests.py
    test_tmp.stream(tmp_args).dump(str(folder / "tests.py"))

    # __init__.py
    init_tmp.stream(tmp_args).dump(str(folder / "__init__.py"))
