import csv

with open("mics.tsv") as file:
    micData = list(csv.reader(file, delimiter="\t", quotechar='"'))

for entry in micData[2:]:
    print(f"{entry[1]}: {entry[0]}")