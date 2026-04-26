def bandingkan(file, file1):
    with open("file.txt", "r") as file, open("file1.txt","r") as file1:
        line = file.readlines()
        line1 = file.readlines()
        baris_max = max(len(line), len(line1))
        for i in range(baris_max):
            lineke1 = line[1].strip() if i < len(line) else None
            lineke2 = line[i].strip() if i < len(line1) else None
            if lineke1 != lineke2:
                print(f"line ke{i+1}")
                if lineke1 is not None:
                    print(f"file 1: {lineke1}")
                else:
                    print("file 1: Tidak ada")
                if lineke2 is not None:
                    print(f"file 2: {lineke2}")
                else:
                    print("file 2: Tidak ada")
                print()
bandingkan("file.txt", "file1.txt")
                