class InvalidAgeError(Exception):
    def __init__(self, message="Aap ki age 18 saal se kam he"):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age<18:
        raise InvalidAgeError()
    print("Access granted")


try:
    user_age = int(input("Please Enter Your Age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Your Age is incorrect")