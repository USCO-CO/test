from users import Users

my_users = []
stop = True
#menu
def add_user ():
	name = input("Enter your name: ")
	pw = input("Enter your password: ")
	new_user = Users(name, pw)
	return new_user

def get_pw ():
	name = input("Enter your name: ")
	return 
while stop:
	print("Press'a' to add a user\n Press 's' to end.")
	select = input()
	if select == ("a" or "A"):
		my_users.append(add_user())
	else:
		stop = False
	
print(my_users)

		
		







