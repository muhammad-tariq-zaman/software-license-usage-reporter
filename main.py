"""Licence usage rate per product.

Usage: python3 main.py licences.csv
CSV columns: software,licences_owned,licences_used.
Usage percent per product, highest usage first; OVERUSED when
used exceeds owned.
"""
import argparse, csv, sys

def report(rows):
    out = []
    for row in rows:
        owned = int(row["licences_owned"])
        used = int(row["licences_used"])
        pct = used / owned if owned else 0
        verdict = "OVERUSED" if used > owned else "OK"
        out.append((row["software"], owned, used, pct, verdict))
    return sorted(out, key=lambda r: -r[3])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for software, owned, used, pct, verdict in report(list(csv.DictReader(f))):
            print(f"{software}: {verdict} ({used}/{owned} used, {pct:.0%})")
    return 0

if __name__ == "__main__":
    sys.exit(main())
