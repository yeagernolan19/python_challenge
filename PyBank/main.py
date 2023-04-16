import csv
import statistics

path = 'Resources/budget_data.csv'

with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    row_count = sum(1 for row in csv_reader)
    print("Total Months: ", row_count)

    csv_file.seek(0)
    next(csv_reader) 

    total = sum(int(row[1]) for row in csv_reader)
    print("Total: $", total)

    csv_file.seek(0)
    next(csv_reader) 
    next(csv_reader) 

    values = []
    for row in csv_reader:
        value = float(row[1])
        values.append(value)
    average = statistics.mean(values)
    print("The average change is: $", round(average, 2))

    csv_file.seek(0)
    next(csv_reader) 
    largest_number = max(float(row[1]) for row in csv_reader)
    csv_file.seek(0)
    next(csv_reader) 
    for row in csv_reader:
        if float(row[1]) == largest_number:
            print('Greatest Increase in Profits:', row[0], '$',largest_number)

    csv_file.seek(0)
    next(csv_reader) 
    lowest_number = min(float(row[1]) for row in csv_reader)
    csv_file.seek(0)
    next(csv_reader) 
    for row in csv_reader:
        if float(row[1]) == lowest_number:
            print('Greatest Decrease in Profits:', row[0], '$',lowest_number)


