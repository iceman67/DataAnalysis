import csv

city = input("Enter city name:")
print("city name %s" % city)

with open("{}.csv".format(city), mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["Date"]}, {row["Temp"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')

