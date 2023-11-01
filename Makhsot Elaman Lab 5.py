#task 1.1
# elaman = input("Enter a string with whitespaces: ")
# elaman2 = elaman.lower().replace(' ', '')
# char_list = list(elaman2)
# print("Created list is:")
# print(char_list)

#task 1.2
# Elaman_list = ['p', 'u', 'l', 'p', 'f', 'i', 'c', 't', 'i', 'o', 'n']
# fr_list = [(char, Elaman_list.count(char)) for char in set(Elaman_list)]
# print("Code Output:")
# print(fr_list)

#task 1.3
# list1 = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]
# vowels = "aeiou"
# list_vow = [(char, freq) for char, freq in list1 if char in vowels]
# list_cons = [(char, freq) for char, freq in list1 if char.isalpha() and char not in vowels]
# list_sym = [(char, freq) for char, freq in list1 if not char.isalnum()]
# print("list_vow =", list_vow)
# print("list_cons =", list_cons)
# print("list_sym =", list_sym)

#task 1.4
# def divide_into_quartiles(list_ela):
#     sorted_list = sorted(list_ela)
#     num_elements = len(sorted_list)
#     quartile_size = num_elements // 4
#
#     q1 = [0] * (quartile_size - num_elements % 4) + sorted_list[:quartile_size]
#     q2 = sorted_list[quartile_size:2 * quartile_size]
#     q3 = sorted_list[2 * quartile_size:3 * quartile_size]
#     q4 = sorted_list[3 * quartile_size:]
#
#     return q1, q2, q3, q4
#
# list_ela1 = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]
# q1, q2, q3, q4 = divide_into_quartiles(list_ela1)
# print("Code Output:")
# print("q1 =", q1)
# print("q2 =", q2)
# print("q3 =", q3)
# print("q4 =", q4)
#
# list_ela2 = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4, 8]
# q1, q2, q3, q4 = divide_into_quartiles(list_ela2)
# print("\nSecond Code Output:")
# print("q1 =", q1)
# print("q2 =", q2)
# print("q3 =", q3)
# print("q4 =", q4)

#task 2.1
#Создаем вводные данные, например студент Еламан
student_name = 'Elaman'
assignment_scores = [82, 56, 44, 30]
lab_scores = [78.20, 77.20]
test_scores = [78, 77]
#Создаем словарь
student = {
    'name': student_name,
    'assignment': assignment_scores,
    'test': test_scores,
    'lab': lab_scores
}
#Вывод
print("student =",student['name'])

#task 2.2
# studentEla = {'name': 'Elaman', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
# submission_rate = 0
# if len(studentEla['assignment']) == 4 and len(studentEla['test']) == 2 and len(studentEla['lab']) == 2:
#     submission_rate = 6
# submission_check = {studentEla['name']: submission_rate}
# print(submission_check)


# #task 2.3
# student = {'name': 'Elaman', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
# submission_rate = {'Elaman': 6}
#
# if student['name'] in submission_rate and submission_rate[student['name']] >= 4:
#     assignment_average = sum(student['assignment']) / len(student['assignment'])
#     lab_average = sum(student['lab']) / len(student['lab'])
#     test_average = sum(student['test']) / len(student['test'])
#     final_grade = 0.3 * assignment_average + 0.5 * lab_average + 0.2 * test_average
#     student['final_grade'] = round(final_grade, 2)
# else:
#     student['final_grade'] = 0
#
# print(student)
#
# student2 = {'name': 'Elzhan', 'assignment': [82, 30], 'test': [], 'lab': [78.2]}
# submission_rate2 = {'Adam': 6, 'Kevin': 3}
#
# if student2['name'] in submission_rate2 and submission_rate2[student2['name']] >= 4:
#     assignment_average2 = sum(student2['assignment']) / len(student2['assignment'])
#     lab_average2 = sum(student2['lab']) / len(student2['lab'])
#     test_average2 = sum(student2['test']) / len(student2['test'])
#     final_grade2 = 0.3 * assignment_average2 + 0.5 * lab_average2 + 0.2 * test_average2
#     student2['final_grade'] = round(final_grade2, 2)
# else:
#     student2['final_grade'] = 0
#
# print(student2)

#task 2.4
# student = {'name': 'Elaman', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
# student2 = {'name': 'Elzhan', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}
#
# students = {student['name']: {'assignment': student['assignment'], 'test': student['test'], 'lab': student['lab'], 'final_grade': student['final_grade']},
#             student2['name']: {'assignment': student2['assignment'], 'test': student2['test'], 'lab': student2['lab'], 'final_grade': student2['final_grade']}}
# print(students)

#task 3.1
# transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]
#
# stats = {}
#
# for user, transaction_type in transactions:
#     if user not in stats:
#         stats[user] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}
#
#     stats[user][transaction_type] += 1
#
#     if stats[user]['mft'] is None or stats[user][transaction_type] > stats[user][stats[user]['mft']]:
#         stats[user]['mft'] = transaction_type
#
#     if stats[user]['lft'] is None or stats[user][transaction_type] < stats[user][stats[user]['lft']]:
#         stats[user]['lft'] = transaction_type
#
# stats = {str(user): stats[user] for user in stats}
#
# print(stats)
#


