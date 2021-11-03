import csv
import yaml

with open("mics.tsv") as file:
    micData = list(csv.reader(file, delimiter="\t", quotechar='"'))

outputArray = []

for x in range(2, len(micData[0])):
    # print("- scene:", micData[0][i])
    cue = {"cue": f"{micData[0][x]} {micData[1][x]}".strip(), "actors": []}
    for y in range(2, len(micData)):
        if micData[y][x] != "":
            # print("  -", micData[j][1])
            cue["actors"].append(micData[y][1])
    outputArray.append(cue)

# print(yaml.dump(outputArray, sort_keys=False))
with open(input("Write to: ")+".yml", "w") as file:
    file.write(yaml.dump(outputArray, sort_keys=False).replace("\n-", "\n\n-"))