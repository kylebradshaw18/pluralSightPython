#prints Hello World
print("Hello World")

t = str("16")
if t == 16:
	print(True)
else:
	print(False)


#Lists
string_list = ["hello", "world"]

#Loop
for s in string_list:
	print(s)


for i in range(2, 10, 3):
	print(i)


x = True
if x:
	x = x != True
else:
	x = x

print(x)


#Dictionaries
student = {
	"name": "Kyle",
	"student_id": 15163,
	"feedback": None
}

student["last_name"] = "Bradshaw"
last_name = None
try:
	last_name = student["last_name"]
except KeyError:
	print("Error finding last name")

print(last_name)