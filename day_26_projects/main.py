# numbers =[1, 2, 3]
# new_numbers = [n+1 for n in numbers]
#
# """prints each letter in list"""
# name = "Navruza"
# letters_list = [letter for letter in name]
#
# range_list = [num *2 for num in range(1,5)]
# list_num = [n for n in range(1,6)]
#
#
# names = ["Alex", "Ben", "Ruby", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name)<5]
# uppercase_name = [name.upper() for name in names if len(name) >=5]
#
#
#
# student_scores = {
#     "Alex": 89,
#     "Ben": 67,
#     "Ruby": 56,
#     "Eleanor": 34,
#     "Freddie": 23
# }
#
#
# names = ["Alex", "Ben", "Ruby", "Eleanor", "Freddie"]
# import random
# student_score = {student:random.randint(1, 100) for student in names}
# passed_students = {student: score for (student, score) in student_score.items() if score >= 60}
#
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: temp * 9 / 5 + 32 for (day, temp) in weather_c.items()}

print(weather_f)

#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through data frame
# for (key value) in student_data_frame.items():
#      print(value)