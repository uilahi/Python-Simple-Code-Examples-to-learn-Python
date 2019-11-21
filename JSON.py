from json.encoder import JSONEncoder
from json.decoder import JSONDecoder
import json

x = [1, "a", True]

print("Original Data :\n", x)

k = json.dumps(x)

print("\nData after Dumping(serializinf :\n", k)


data_to_write = "*******************"
path = "C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\"
with open(path+"demo_write.txt","w") as f:
    json.dump(x, f)
    f.closed

path = "C:\\Users\\Umair.ilahi\\python_workspace\\Python_Bootcamp_Full_Syllabus\\FileHandling\\"
with open(path+"demo_write.txt") as f:
    z = json.load(f)
    f.closed
print("\nAfter reconstructing Data from File :\n", z)


colour_dict = { "colour": ["red", "yellow", "green" ]}
print("\nOriginal color_dict:\n", colour_dict)
# directly called encode method of JSON
aa = JSONEncoder().encode(colour_dict)
print("\n After using JSONEncoding :\n", aa)

bb = JSONDecoder().decode(aa)
print("\n After using JSONDecoding :\n", bb)

