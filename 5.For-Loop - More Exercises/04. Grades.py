students = int(input())

grade_5 = 0
grade_4 = 0
grade_3 = 0
fail = 0
gpa = 0

for student in range(students):
    grade = float(input())
    gpa += grade #  така предполагам, че ще гръмне на някой от тестовете!
    if 2.00 <= grade <= 2.99:
        fail += 1
    elif 3.00 <= grade <= 3.99:
        grade_3 += 1
    elif 4.00 <= grade <= 4.99:
        grade_4 += 1
    else:
        grade_5 += 1

print('Top students: %.2f' % ((grade_5 / students) * 100) + '%')
print('Between 4.00 and 4.99: %.2f' % ((grade_4 / students) * 100) + '%')
print('Between 3.00 and 3.99: %.2f' % ((grade_3 / students) * 100) + '%')
print('Fail: %.2f' % ((fail / students) * 100) + '%')
print('Average: %.2f' % (gpa / students))