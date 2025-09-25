import csv

filepath = "miscelanious/people-100.csv"

fields = []
rows = []

with open(filepath, 'r') as file:
    reader = csv.reader(file)
    
    
    fields = next(reader)
    rows = list(reader)
    
    
    for n, field in enumerate(fields):
        
        print("\n", field)
        for i, row in enumerate(rows):
            if i == 5:
                break
            print(row[n])