class User():
	"""This is a class for Users"""
	def __init__(self, f_name, l_name):
		self.f_name = f_name
		self.l_name = l_name
		self.login_attempts = 0

	def describe_user(self):
		print("First Name: "+self.f_name.title()+"\nLast Name: "+self.l_name.title())

	def greet_user(self):
		print("Hello "+self.f_name.title()+" "+self.l_name.title()+".")

	def increment_login_attemps(self):
		self.login_attempts += 1

	def reset_login_attemps(self):
		self.login_attempts = 0

my_user = User('Abdullah', 'Shah')
my_user.describe_user()
my_user.greet_user()



class Priveleges:
	"""Class defining priveleges a user would have"""
	def __init__(self, priveleges):
		self.priveleges = priveleges

	def show_privileges(self):
		for privelege in self.priveleges:
			print(privelege)

class Admin(User):
	"""Class for special kinds of users, Admins"""
	def __init__(self, f_name, l_name, priveleges):
		super().__init__(f_name,l_name)
		self.priveleges = Priveleges(priveleges)

my_admin = Admin("Abdullah","Shah",["Add Users", "Delete Uses", "Modify Users"])
## my_admin.show_privileges()

my_admin2 = Admin("Jamal", "Shah", ["X-Ray Vision","Flight","Bullet Immunity"])
my_admin2.priveleges.show_privileges()
