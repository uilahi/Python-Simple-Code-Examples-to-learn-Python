import pandas as pd

try:
    df = pd.read_csv(
        "C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\demo_write.txt",
        delimiter=',')
    df.to_csv('C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\new.csv')

except FileNotFoundError:
    print("File Not FOund")

else:
    print("File Present")

finally:
    print("Executed Try Catch")



