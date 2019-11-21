def func111():
    print("Function from One.py")

print("Global print form One.py")

if __name__ == '__main__':
    print("One.py was run directly")
else:
    print("One.py was imported......!!!!!")
    print(__name__)

