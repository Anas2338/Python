class Logger:
    def __init__(self):
        print("object created")

    def __del__(self):
        print("object destroyed")

obj1 = Logger()


