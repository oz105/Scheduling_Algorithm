import pandas
import xlrd
from xlrd import open_workbook
from Student import Student



# 1 - פנימית
# 2 - סיעוד המבוגר כירורגי
# 3 - קידום הבריאות
# 4 - טראומה מלר"ד\מיון
# 5 - סיעוד הקהילה
# 6 - סיעוד האישה
# 7 - סיעוד הילד
# 8 - סיעוד בריאות הנפש
# 9 - סטאז'

b_b = ["ס.המבוגר פנימית", 2]
b_c = [3, 4, 5]
c_a = [4, 5, 6, 7]
c_b = [8]
c_c = [9]
d = [9]


if __name__ == '__main__':

    students_excel = pandas.read_excel('C:\\Users\\user\\Desktop\\algo\\students.xlsx')
    n_rows = len(students_excel.index)
    n_cols = len(students_excel.columns)

    students = []

    for row in range(0, n_rows):
        id_num = students_excel.iloc[row][0]
        full_name = students_excel.iloc[row][1] + " " + students_excel.iloc[row][2]
        year = students_excel.iloc[row][5]
        city = students_excel.iloc[row][6]
        if year == 'ב':
            lst = b_b

        elif year == 'ג':
            lst = c_a

        elif year == 'ד':
            lst = d

        s = Student(id_num, full_name, city, year, lst)
        print(s)
        students.append(s)

    hospitals_excel = pandas.read_excel('C:\\Users\\user\\Desktop\\algo\\Hospitals.xlsx')
    n_rows = len(hospitals_excel.index)
    n_cols = len(hospitals_excel.columns)

    for s in students:
        for row in range(0, n_rows - 1):
            city_to_check = hospitals_excel.iloc[row][0]

            if s.city == city_to_check:
                experience_name = hospitals_excel.iloc[row][2] + " " + hospitals_excel.iloc[row][3]
                print(experience_name)
                if experience_name in s.to_do:






