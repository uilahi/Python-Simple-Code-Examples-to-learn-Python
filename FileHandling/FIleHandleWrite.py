data_to_write = "*******************"
path = "C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\"
with open(path+"demo_write.txt","w") as f:
    f.write(data_to_write)
    f.closed
