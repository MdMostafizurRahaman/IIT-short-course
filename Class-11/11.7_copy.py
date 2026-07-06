source_file = open("output.txt", "r")
content = source_file.read()
source_file.close()

destination_file = open("copy_output.txt", "w")
destination_file.write(content)
destination_file.close()
