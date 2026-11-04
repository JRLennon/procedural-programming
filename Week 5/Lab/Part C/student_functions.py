import csv
from tabulate import tabulate # external module, import through `pip install -r requirements.txt`

def read_csv(filename):
    # read the csv file and return its headings and student records.
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headings = reader.fieldnames
        records = list(reader)

    return headings, records

def display_total(records):
    print(f"Total student records: {len(records)}")

def display_headings(headings):
    print(", ".join(headings))

def display_records(records):
    if not records:
        print("No student records to display.")
        return

    print(tabulate(records, headers="keys", tablefmt="grid"))
