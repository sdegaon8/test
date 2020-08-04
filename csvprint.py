import csv
 
def print_users():
    with open("ASXListedCompanies1.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print("{}".format(row['Company name']))
