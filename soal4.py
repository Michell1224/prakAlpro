filename = input("nama file:")
d = dict()
try:
    file = open(filename)
except:
    print("File tidak terbuka", filename)
    quit()
for line in file:
    if line.stsrtwith('form'):
        word = line.split()
        email = word[1]
        d[d] = d.get(d, 0)+1
    file.close()
print(d)