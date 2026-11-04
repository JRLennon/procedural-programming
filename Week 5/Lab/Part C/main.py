from student_functions import read_csv, display_total, display_headings, display_records

filename = "dataset.csv"

try:
    headings, records = read_csv(filename)

    while True:
        print("\nChoose what to display:")
        print("1. Total number of student records")
        print("2. Column headings")
        print("3. All student records")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_total(records)
        elif choice == "2":
            display_headings(headings)
        elif choice == "3":
            display_records(records)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

except FileNotFoundError: # give generic error if the dataset CSV file is not there
    print(f"Could not find {filename} - Ensure it is named correctly, and in the same directory as main.py.")
