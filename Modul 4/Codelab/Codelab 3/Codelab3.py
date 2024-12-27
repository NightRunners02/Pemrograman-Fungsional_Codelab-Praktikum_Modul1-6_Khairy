def simple_decorator(func):
    def wrapper():
        print("Fungsi ini dipanggil")
        func()
    return wrapper


@simple_decorator
def hello():
    print("Hello, World!")

hello()

