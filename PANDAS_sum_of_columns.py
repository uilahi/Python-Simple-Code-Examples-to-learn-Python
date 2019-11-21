import pandas as pd
df = pd.read_csv(
        "C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\demo_write.txt",
        delimiter=',')
df.to_csv('C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\new.csv')
