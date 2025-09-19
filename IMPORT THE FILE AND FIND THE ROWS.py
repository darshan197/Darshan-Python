import csv

filename = input("Enter the CSV file path: ")

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    row_count = sum(1 for row in reader)

print(f"Number of rows in the file: {row_count}")