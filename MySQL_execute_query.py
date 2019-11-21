import mysql.connector
import pandas

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root",
  database="classicmodels",
)

mycursor = mydb.cursor()

mycursor.execute('''SELECT `employees`.`lastName`, COUNT(*) as 'Total customers' from customers 
                 JOIN employees ON `customers`.`salesRepEmployeeNumber` =  `employees`.`employeeNumber` 
                 GROUP BY `employees`.`lastName`;'''
                 )

myresult = mycursor.fetchall()
with open("C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\MYSQLtoCSV.txt", "w") as f:

    for x in myresult:
        temp = (str(x).strip('('))
        f.write(temp.strip(')')+"\n")
        print(x)
    f.closed

df = pandas.read_csv("C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\MYSQLtoCSV.txt", delimiter=',')
df.to_csv("C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\MYSQLtoCSV.csv")