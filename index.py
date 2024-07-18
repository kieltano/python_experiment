user_name = None
user_age = None

def welcome():
    print("Hello, My name is buddy! Glad to meet ya.")
    what_is_your_name()

def what_is_your_name():
    global user_name
    print("What is your name?")
    name = input("")
    print(f"Nice to meet you {name}!")
    user_name = name
    what_is_your_age()
    return name

def what_is_your_age():
    global user_age
    print("How old are you?")
    age = int(input(""))
    user_age = age
    age_calculator()
    return age


def age_calculator():
    futur_age = user_age + 10
    print(f"In 10 years you are going to be {futur_age} years old")
    thank_message()


def thank_message():
    print("Thank You")
    print(f"See You next time {user_name}.")

# Start the prgram
welcome()
