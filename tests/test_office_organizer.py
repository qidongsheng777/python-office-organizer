from pathlib import Path

from office_organizer.organizer import category_for_file, organize_files
from office_organizer.table_summary import summarize_tables


def test_category_for_file():
    assert category_for_file(Path("report.docx")) == "documents"
    assert category_for_file(Path("data.xlsx")) == "spreadsheets"
    assert category_for_file(Path("photo.png")) == "images"
    assert category_for_file(Path("backup.zip")) == "archives"
    assert category_for_file(Path("unknown.bin")) == "others"


def test_organize_files(tmp_path):
    source = tmp_path / "source"
    output = tmp_path / "output"
    source.mkdir()
    (source / "resume.docx").write_text("demo", encoding="utf-8")
    (source / "scores.csv").write_text("name,score\nA,90\n", encoding="utf-8")

    results = organize_files(source, output, keywords=["resume"])

    assert len(results) == 2
    assert (output / "documents" / "keyword_resume" / "resume.docx").exists()
    assert (output / "spreadsheets" / "scores.csv").exists()


def test_summarize_tables(tmp_path):
    source = tmp_path / "tables"
    source.mkdir()
    (source / "scores.csv").write_text("name,score\nA,90\nB,\n", encoding="utf-8")
    output_csv = tmp_path / "summary.csv"

    summaries = summarize_tables(source, output_csv)

    assert len(summaries) == 1
    assert summaries[0].rows == 2
    assert summaries[0].columns == 2
    assert summaries[0].empty_cells == 1
    assert output_csv.exists()
