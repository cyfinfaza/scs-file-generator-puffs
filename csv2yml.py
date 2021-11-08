import csv
import yaml

with open(input("Input File: ")) as file:
    micData = list(csv.reader(file, delimiter="\t", quotechar='"'))

outputArray = []

START_X = 3
START_Y = 2


for x in range(START_X, len(micData[0])):
    # print("- scene:", micData[0][i])
    cue = {"cue": f"{micData[0][x]} {micData[1][x]}".strip(), "actors": []}
    for y in range(START_Y, len(micData)):
        if micData[y][x].strip() != "" and micData[y][x].strip()[:2] != "//":
            # print("  -", micData[j][1])
            cue["actors"].append(micData[y][1].strip())
    outputArray.append(cue)

# print(yaml.dump(outputArray, sort_keys=False))
with open(input("Write to: ")+".yml", "w") as file:
    file.write(yaml.dump(outputArray, sort_keys=False).replace("\n-", "\n\n-"))