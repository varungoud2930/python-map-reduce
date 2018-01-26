i = open("purchases.txt", "r")
o = open("o.txt", "w")

lines = readlines()
for line in i:
  data = line.strip().split('    ')
  if (len(data) == 6):
    date, time, store, item, cost, payment = data
    print store, "\t", cost
    o.write(store + "\t" + cost+ "\n")

i.close()
o.close()
