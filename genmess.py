import csv, random, sys

ninsts = int(sys.argv[1])
ngood = int(sys.argv[2])
nrand = int(sys.argv[3])

writer = csv.writer(sys.stdout)

def flip(p):
    return int(random.random() < p)

good_schemas = [flip(0.5) for _ in range(ngood)]

def flip_good(cl, f, p):
    fl = flip(p)
    ok = int(cl == fl)
    if good_schemas[f] == 0:
        return 1 - ok
    else:
        return ok

def genrow(i):
    label = i
    cl = flip(0.5)
    goods = [flip_good(cl, f, 0.7) for f in range(ngood)]
    rands = [flip(0.5) for _ in range(nrand)]
    writer.writerow([label, cl] + goods + rands)

for i in range(ninsts):
    genrow(i)
