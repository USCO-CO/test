#!/usr/bin/python
# users
# Created by Jeff Cooper on 9/25/16.

class Users:
	def __init__(self, name, password):
		self.name = name
		self.password = password

	def __repr__(self):
		return "<User Name {}>".format(self.name)
	
	def save_file(self):
		with open("user_pw.txt", 'w') as f:
			f.write(self.name + "," + self.password + ",")
	def append_file(self):
		with open("user_pw.txt", 'a') as f:
			f.write(self.name + "," + self.password + ",")
	
	def load_from_file(self):
		with open("user_pw.txt", 'r') as f:
			content = f.readlines()	
			for line in content:
				movie_data = line.split(",")
				#print (movie_data)
				movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))
				print(movies)
			user = User(username)
			user.movies = movies
			return user
				

		
		