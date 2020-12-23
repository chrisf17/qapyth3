def include(name):
    
    return len(name) > 3

names = ["Fred", "Amy", "Bob", "Suzy", "Beth", "Tom"]

# TODO 1: Rewrite the below code as a function
included_names = []
for name in names:
    if include(name):
        included_names.append(name)

# TODO 2: How might we make the inclusion criteria more flexible?
#         The caller of your new function might want to specify their own inclusion criteria and that  #         might not be based on name length!


# TODO 3: Rewrite all of the code to use the built-in filter function. Concise is good!

        
