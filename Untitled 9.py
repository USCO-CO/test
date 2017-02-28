s = input()
key = input()
a = set ()
for i in range (0, len(s)-1):
	if s.find(key,i) != -1:
		a.add(s.find(key,i))
	
print (len(a))



