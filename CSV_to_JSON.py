import pandas as pd

df= pd.read_csv("C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\csv_from_json.csv")

df.to_json("C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\json_from_csv.json")
try:
    with open("C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\json_from_csv.json", "r") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("FIle Not FOund")
else:
    print("Found FIle")


