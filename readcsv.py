import csv

print(csv.list_dialects())

def reader():
    with open("StockQuotes.csv") as datafile:
        reader = csv.reader(datafile)
        for row in reader:
            print(row)

def useSniffer():
    with open("Namelist.csv") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        hasHeader = csv.Sniffer().has_header(csvfile.read(1024))
        csvfile.seek(0)
        print("Headers found: " + str(hasHeader))
        print(dialect.delimiter)
        print(dialect.escapechar)
        print(dialect.quotechar)

def writerSample():
    with open("SampleData.csv", mode="w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Name", "Department", "Location"])
        csvwriter.writerow(["John", "Accounting", "New York"])
        csvwriter.writerow(["Jane", "Human Resources", "New York"])
        csvwriter.writerow(["Daniel", "Engineering", "New York"])

