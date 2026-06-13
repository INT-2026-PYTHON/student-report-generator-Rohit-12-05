"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.

from .stats import average_per_student, subjects_offered, top_scorer, passing_students

# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    total_records = len(records)
    subjects = sorted(list(subjects_offered(records))) 
    
    averages = average_per_student(records)
    top_name, top_avg = top_scorer(records)
    passing = passing_students(records)

    avg_lines = []
    for name in sorted(averages.keys()):
        avg_lines.append(f"  {name} : {averages[name]}")
    avg_str = "\n".join(avg_lines)

    report = (
        "=== Gradebook Report ===\n"
        f"Total records: {total_records}\n"
        f"Subjects offered: {', '.join(subjects)}\n\n"
        "Averages:\n"
        f"{avg_str}\n\n"
        f"Top scorer: {top_name} ({top_avg})\n"
        f"Passing students (>= 60.0): {', '.join(passing)}"
    )
    
    return report
    
    # TODO: implement
    pass
