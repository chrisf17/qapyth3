def include(name):
    
    return len(name) > 3


names = ["Fred", "Amy", "Bob", "Suzy", "Beth", "Tom"]

# TODO 1: Rewrite the below code as a function and write some code to test it

included_names = []
for item in names:
    if len(item) > 3:
        included_names.append(item)

print(included_names)


# TODO 2: How might we make the inclusion criteria more flexible?
#         The caller of your new function might want to specify their own inclusion criteria and that  #         might not be based on name length!


# TODO 3: Rewrite all of the code to use the built-in filter function. Concise is good!


