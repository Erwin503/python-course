def avg(grades, students):
    grades_len = len(grades)
    stud_len = len(students)
    if (grades_len != stud_len):
        return 'input err'
    
    res = {}
    grade_num = 0

    for student in students:
        res[student] = sum(grades[grade_num]) / len(grades[grade_num])
        grade_num += 1
    
    return res


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(avg(grades, students))