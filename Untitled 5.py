#from decimal import Decimal
n = int(input())
studentsList = []
for i in range(0,n):
	student = input().strip().split(" ")
	studentsList.append( {'name':student[0], "math":float(student[1]), 	"physics":float(student[2]), "chemistry":float(student[3])})

testName = input()
testName = (next(item for item in studentsList if item["name"] == testName))
print("%.2f" % (( (testName.get('physics'))+(testName.get('chemistry'))+(testName.get('math')))/3))



