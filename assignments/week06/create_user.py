def create_user_profile(username, age=18, premium=False):
    status = "Premium User" if premium else "Standard User"
    return f"{username} (age: {age}) - {status}"


print(create_user_profile("Supawit", 19, True))
print(create_user_profile("Tab", 20))
print(create_user_profile("Benya", 18, True))