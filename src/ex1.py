# from ValidationException import ValidationException
#
#
# def validate_file(input_file):
#     with open(input_file) as mile_file:
#         next(mile_file)
#         for line_num, line in enumerate(mile_file, start=2):
#             car_id, mileage = line.split(',')
#             try:
#                 mileage = int(mileage)
#             except ValueError:
#                 print("Invalid mileage: " + str(mileage))
#
# def ex1():
#     # try:
#         validate_file("../files/input.txt")
#     # except ValidationException as ve:
#     #     print(ve)
#
# ex1()
#


#________________________________________________OR

from ValidationException import ValidationException

def validate_file(file_name):
    with open(file_name, "r") as file1:
        next(file1)
        #To check if its running:
        #print(file1.read())

             #index  value
        for count, line in enumerate(file1):
            # print(count, line)
            line_values = line.split(',')
            # print(line_values)

            #if second value is a number if it is not a number -> throw exception
            try:
                int(line_values[1])
            except:
                raise ValidationException(f"invalid mileage:{line_values[1]}")
            # print(int(line_values[1]))
            # finally:



def ex1():
    try:
        validate_file("../files/input.txt")
    except ValidationException as ve:
        print(ve)

ex1()