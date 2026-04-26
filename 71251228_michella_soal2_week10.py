filename = "file.txt"
try:
    with open(filename, "r") as file:
        print(f"namefile1: {filename}")

        for line in file:
            if "| |" in line:
                bagian = line.split("| |")
                question = bagian[0].strip()
                answer = bagian[1].strip()
                print(f"question: {question}")
                input = input("answer: ")
                if input.lower() == answer.lower():
                    print("jawaban benar")
                else:
                    print(f"jawaban salah")
except FileNotFoundError:
    print(f"Error: file '{filename}' tidak ditemukan")
