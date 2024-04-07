
authorized = False
password = "nika398"


while authorized != "true":
    user_input = input("please enter your password: ")
    if user_input == "nika398":
        print("accses granted")
        authorized = "true"