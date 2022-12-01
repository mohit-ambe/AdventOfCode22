file = open("input.txt", "r")
myin = [line.strip() for line in file.readlines() if not line.isspace()]
file.close()
print(myin)
