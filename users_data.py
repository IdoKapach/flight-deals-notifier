import requests

# this class is responsible for getting the users' information - first name, last name and email, from the
# sheet that contains this information
class UsersData():

    def post(self, first_name, last_name, email):
        users_emails = [user["email"] for user in self.get()]
        if email not in users_emails:
            data_dict = {
                'user' : {
                    'firstName': first_name,
                    'lastName': last_name,
                    'email': email
                }
            }

            response = requests.post("https://api.sheety.co/194a903f2d68efdf228c542aab1e2357/day40Python/users", json=data_dict)
            response.raise_for_status()
        else:
            raise "this email is already registered in the system"

    def get(self) -> list:
        response = requests.get("https://api.sheety.co/194a903f2d68efdf228c542aab1e2357/day40Python/users")
        return response.json()["users"]

