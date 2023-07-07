import csv

def find_total_ones():
    total_ones = 0
    file_paths = ["../files/week-1.csv", "../files/week-2.csv", "../files/week-3.csv"]
    for file in file_paths:
        with open(file, "r") as csv_file:
            rows = csv.reader(csv_file, delimiter=',')
            next(rows)  # Skip the header row
            for row in rows:
                for value in row[1:]:
                    total_ones += int(value)
    return total_ones

def ex2():
    total_ones = find_total_ones()
    print(f"Total ones: {total_ones}.")

ex2()
#Hello Imane <3