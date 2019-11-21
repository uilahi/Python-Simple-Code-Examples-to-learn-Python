import pandas as pd
import json

df= pd.read_json("C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\json_for_csv.json")

df.to_csv("C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\csv_from_json.csv")
