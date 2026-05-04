# Setting "Guest" as the default value for the 'name' parameter
def greet_with_default(name="Guest"):
    print("Welcome,", name)

# Calling without providing an argument (Python uses the default "Guest")
greet_with_default()

# Calling with an argument (Overrides the default value)
greet_with_default("Bob")