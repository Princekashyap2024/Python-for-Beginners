# Problem :- Write a function that greets a user. if no name is provided, it should greet with a default name.

def greet(name = "dear"):
    return f"Hello, {name}!"

print(greet())