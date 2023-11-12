import csv, sys

reader = csv.reader(sys.stdin)

cl_counts = [0, 0]
counts = None
nfeatures = None

for row in reader:
    label = int(row[0])
    cl = int(row[1])
    cl_counts[cl] += 1
    features = [int(f) for f in row[2:]]
    if counts is None:
        nfeatures = len(features)
        print(nfeatures)
        counts = [[0, 0] for _ in range(nfeatures)]
    for i, f in enumerate(features):
        counts[i][int(cl == f)] += 1

print(cl_counts)
for i in range(nfeatures):
    print(i, counts[i][1] / (counts[i][0] + counts[i][1]))
