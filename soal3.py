filename = input("Nama file:")
d = dict()
try:
    file =open(filename)
except:
    print("File tidak bisa terbuka")
    quit()
for line in file:
    line = line.strip()
    if line.startswith('from'):
        word = line.split
        email = word[1]
        d[email] = d.get(email,0)+1
file.close()
print(d)