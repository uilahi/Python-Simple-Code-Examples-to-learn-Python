data_to_write = "*******************"
path = "C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\"
with open(path+"demo1.txt") as f:
    first_line = f.readline()
    read_data = f.read()
    all_lines = f.readlines()
    f.closed
# print(read_data)
# print(first_line)

for line in read_data:
    print(line, end='')
print(f.tell())