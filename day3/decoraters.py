def announce(f):
    def wrapper():
        print('About the run funtion')
        f()
        print("done with function")

    return wrapper

@announce
def hello():
    print("hello world")

hello()