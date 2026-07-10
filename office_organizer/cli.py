from __future__ import annotations

import argparse
from pathlib import Path

from .organizer import organize_files
from .table_summary import summarize_tables


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="office-organizer",
        description="Organize files and summarize CSV/Excel tables for office workflows.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    organize = subparsers.add_parser("organize", help="Classify files into folders.")
    organize.add_argument("source", type=Path, help="Folder containing messy files.")
    organize.add_argument("output", type=Path, help="Folder for organized files.")
    organize.add_argument("--by-date", action="store_true", help="Group files by modified month.")
    organize.add_argument(
        "--keyword",
        action="append",
        default=[],
        help="Keyword to create extra keyword folders. Can be repeated.",
    )
    organize.add_argument("--move", action="store_true", help="Move files instead of copying them.")

    summarize = subparsers.add_parser("summarize", help="Summarize CSV and XLSX files.")
    summarize.add_argument("source", type=Path, help="Folder containing CSV/XLSX tables.")
    summarize.add_argument("output_csv", type=Path, help="Summary CSV output path.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "organize":
        results = organize_files(
            args.source,
            args.output,
            by_date=args.by_date,
            keywords=args.keyword,
            copy=not args.move,
        )
        print(f"Organized {len(results)} files into {args.output}")
    elif args.command == "summarize":
        summaries = summarize_tables(args.source, args.output_csv)
        print(f"Summarized {len(summaries)} table(s) into {args.output_csv}")


if __name__ == "__main__":
    main()
