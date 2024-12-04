# Problem :- Create a function that accepts any number of keyword arguments and print them in the format "key: value".

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(power = "lazer", name = "Shaktiman")
print_kwargs(power = "lazer")
print_kwargs(power = "lazer", name = "Shaktiman")
print_kwargs(name = "Shaktiman")
enemy = "Dr. jackaal"