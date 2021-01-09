current_users = ["john", "peter", "paul", "Grace", "luke"]
new_users = ["luke", "Lois", "Paul", "mary", "Eva"]
current_users_lower = [users.lower() for users in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Hi {new_user}, this user is taken, please enter another username")
    else:
        print(f"Hi {new_user}, the username is available")
