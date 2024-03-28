user_input = input("Nazwa użytkownika:")
if user_input:
    name = user_input
else:
    name = "Brak nazwy"
    print("Brak nazwy")
    
user_password = input("Hasło")
if user_password:
    password = user_password
else:
    password = "Brak hasła"
    print("Brak hasła")
    print("Odmowa dostępu")
