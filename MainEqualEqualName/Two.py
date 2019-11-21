from Python_Bootcamp_Full_Syllabus.MainEqualEqualName.One import func111

def func222():
    print("Function from Two.py")

print("Global print form Two.py")

func111()

if __name__ == '__main__':
    print("Two.py was run directly")
else:
    print("Two.py was imported......!!!!!")
