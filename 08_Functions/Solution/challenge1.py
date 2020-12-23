def include(name):
    
    return len(name) > 3


names = ["Fred", "Amy", "Bob", "Suzy", "Beth", "Tom"]

# TODO 1: Rewrite the below code as a function and write some code to test
# Should return ['Fred', 'Suzy', 'Beth']
def my_filter(items):
    included_names = []
    for item in items:
        if include(item):
            included_names.append(item)
    return included_names

print(my_filter(names))

# TODO 2: How might we make the inclusion criteria more flexible?
#         The caller of your new function might want to specify their own inclusion criteria and that  #         might not be based on name length!
def my_filter(criteria, items):
    included_names = []
    for item in items:
        if criteria(item):
            included_names.append(item)
    return included_names

print(my_filter(include, names))

# TODO 3: Call your function to filter names to return only names containing an 'e'
# Use a lambda rather than write a new filtering function
print(my_filter(lambda n:"e" in n, names))

# TODO 3: Rewrite all of the code to use the built-in filter function and display the results!
print(filter(lambda n:"e" in n, names))
print(list(filter(lambda n:"e" in n, names)))
for name in filter(lambda n:"e" in n, names):
    print(name)


        
