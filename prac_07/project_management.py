"""
Project Management Program
Estimate: 60 minutes
Actual:
"""

from __future__ import annotations
from datetime import datetime, date
import csv
from typing import List
from project import Project

DEFAULT_FILE = "projects.txt"

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
>>> """

def main() -> None:
    projects = load_projects(DEFAULT_FILE)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {DEFAULT_FILE}")
    while True:
        choice = input(MENU).strip().lower()
        if choice == "l":
            fname = input("Filename to load: ").strip() or DEFAULT_FILE
            projects = load_projects(fname)
            print(f"Loaded {len(projects)} projects from {fname}")
        elif choice == "s":
            fname = input("Filename to save to: ").strip() or DEFAULT_FILE
            save_projects(projects, fname)
            print(f"Saved {len(projects)} projects to {fname}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            # offer to save on quit
            if input("Save to default file before quitting? [Y/n] ").strip().lower() in ("", "y"):
                save_projects(projects, DEFAULT_FILE)
            break
        else:
            print("Invalid option.")


def parse_date(dmy: str) -> date:
    return datetime.strptime(dmy.strip(), "%d/%m/%Y").date()

def load_projects(filename: str = DEFAULT_FILE) -> List[Project]:
    projects: List[Project] = []
    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)  # skip header
        for name, start_str, priority_str, cost_str, completion_str in reader:
            projects.append(
                Project(
                    priority=int(priority_str),
                    start_date=parse_date(start_str),
                    name=name,
                    cost_estimate=float(cost_str),
                    completion=int(completion_str),
                )
            )
    return projects


def save_projects(projects: List[Project], filename: str = DEFAULT_FILE) -> None:
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for p in projects:
            writer.writerow([
                p.name,
                p.start_date.strftime("%d/%m/%Y"),
                p.priority,
                f"{p.cost_estimate:.0f}" if p.cost_estimate.is_integer() else f"{p.cost_estimate}",
                p.completion,
            ])

def display_projects(projects: List[Project]) -> None:
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete   = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p.format_line()}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p.format_line()}")

def filter_by_date(projects: List[Project]) -> None:
    date_str = input("Show projects that start after date (dd/mm/yy): ")
    try:
        after = parse_date(date_str)
    except ValueError:
        print("Invalid date.")
        return
    filtered = sorted([p for p in projects if p.start_date >= after], key=lambda p: p.start_date)
    for p in filtered:
        print(f"  {p.format_line()}")

def add_new_project(projects: List[Project]) -> None:


def update_project(projects: List[Project]) -> None:


















if __name__ == "__main__":
    main()