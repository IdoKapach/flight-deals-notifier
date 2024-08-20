from users_data import UsersData
#  program that registers users
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
email = input("enter your email: ")

data = UsersData()
data.post(first_name, last_name, email)