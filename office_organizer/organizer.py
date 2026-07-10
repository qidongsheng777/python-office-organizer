from __future__ import annotations

import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DOCUMENT_EXTENSIONS = {".doc", ".docx", ".pdf", ".txt", ".md"}
SPREADSHEET_EXTENSIONS = {".xls", ".xlsx", ".csv", ".tsv"}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}
ARCHIVE_EXTENSIONS = {".zip", ".rar", ".7z", ".tar", ".gz"}


@dataclass(frozen=True)
class OrganizedFile:
    source: Path
    destination: Path
    category: str


def category_for_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in DOCUMENT_EXTENSIONS:
        return "documents"
    if suffix in SPREADSHEET_EXTENSIONS:
        return "spreadsheets"
    if suffix in IMAGE_EXTENSIONS:
        return "images"
    if suffix in ARCHIVE_EXTENSIONS:
        return "archives"
    return "others"


def month_bucket(path: Path) -> str:
    modified = datetime.fromtimestamp(path.stat().st_mtime)
    return modified.strftime("%Y-%m")


def keyword_bucket(path: Path, keywords: list[str]) -> str | None:
    lowered = path.name.lower()
    for keyword in keywords:
        cleaned = keyword.strip().lower()
        if cleaned and cleaned in lowered:
            return cleaned
    return None


def unique_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    parent = destination.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def organize_files(
    source_dir: Path,
    output_dir: Path,
    *,
    by_date: bool = False,
    keywords: list[str] | None = None,
    copy: bool = True,
) -> list[OrganizedFile]:
    if not source_dir.exists():
        raise FileNotFoundError(f"Source folder does not exist: {source_dir}")
    if not source_dir.is_dir():
        raise NotADirectoryError(f"Source path is not a folder: {source_dir}")

    keywords = keywords or []
    output_dir.mkdir(parents=True, exist_ok=True)
    organized: list[OrganizedFile] = []

    for item in sorted(source_dir.iterdir()):
        if not item.is_file():
            continue

        category = category_for_file(item)
        parts = [category]
        keyword = keyword_bucket(item, keywords)
        if keyword:
            parts.append(f"keyword_{keyword}")
        if by_date:
            parts.append(month_bucket(item))

        target_folder = output_dir.joinpath(*parts)
        target_folder.mkdir(parents=True, exist_ok=True)
        destination = unique_destination(target_folder / item.name)

        if copy:
            shutil.copy2(item, destination)
        else:
            shutil.move(str(item), destination)

        organized.append(OrganizedFile(item, destination, category))

    return organized
