files = ["data1.csv", "image.png", "data_report.csv", "summary.txt", "data.csv"]

for file in files:
    if file.startswith("data") and file.endswith(".csv"):
        print(file)