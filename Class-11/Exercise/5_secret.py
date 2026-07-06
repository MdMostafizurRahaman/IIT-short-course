import os

files = os.listdir(".") 
total_secret_count = 0

for file in files:
    if file.endswith(".txt"):
        with open(file, "r") as f:
            content = f.read() 
            lower_content = content.lower() 
            total_secret_count += lower_content.count("secret")

print("The word 'secret' appears", total_secret_count, "times across all text files.")