import csv

crimes = [row[5] for row in csv.reader(open("Crimes.csv"))]
print(max(set(crimes), key=lambda x: crimes.count(x)))

"""
p_type = {}
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if "2015" in row[2]:
            if row[5] not in p_type:
                p_type[row[5]] = 0
            p_type[row[5]] += 1

p_k, p_v = "", 0
for k, v in p_type.items():
    if p_v <= v:
        p_k = k
        p_v = v
print(p_k, p_v)
"""
