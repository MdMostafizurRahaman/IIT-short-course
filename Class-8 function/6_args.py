# *args allows you to pass an unlimited number of regular arguments
def sum_all(*numbers):
    total = sum(numbers)
    print("Total sum of all numbers:", total)

sum_all(5, 10)
sum_all(1, 2, 3, 4, 5, 6, 7)

# **kwargs allows you to pass an unlimited number of labeled (keyword) arguments
def show_student_info(**details):
    print("Student Profile:", details)

show_student_info(name="Rahim", age=21, city="Dhaka")