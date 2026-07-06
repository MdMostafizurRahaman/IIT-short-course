import os

files = os.listdir(".")
combined_content = ""

for file in files:
    if file.endswith(".csv") and file != "combined.csv":
        with open(file, "r") as f:
            combined_content += f.read() + "\n"

with open("combined.csv", "w") as output_file: 
    output_file.write(combined_content) 

print("All CSV files merged into combined.csv")