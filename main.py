import pandas

from Student import Student


def custom_style(row):
    color = 'yellow'
    return pandas.Series('background-color: green', row.index)
    #return ['background-color: %s' % color]*len(row.values)


def create_list_students() -> list:
    students_object = []

    for row in range(n_rows_student):  # change to 10 for check should be row
        experience_lst = []
        flag_year = True
        id_num = students_excel.iloc[row][0]
        full_name = students_excel.iloc[row][1] + " " + students_excel.iloc[row][2]
        year = students_excel.iloc[row][5]
        city = students_excel.iloc[row][6]  # Hebrew

        if year == 'א':
            flag_year = False

        elif year == 'ב':
            experience_lst = experience_by_year.get("B")

        elif year == 'ג':
            experience_lst = experience_by_year.get("C")

        else:
            experience_lst = experience_by_year.get("D")

        if flag_year:
            student = Student(id_num, full_name, city, year, experience_lst, cities_less_50_km_heb.get(city))
            students_object.append(student)
            #print(f"exexperience_lst of student id {id_num} is {experience_lst}")

    return students_object


def write_comment(student): # This function is responsible for writing the column "הערות" in the output Excel
    if len(student.to_do) == 0:
        output_excel.at[row_of_output, 'הערות'] = "הסטודנט שובץ בהכל"

    else:
        size = num_of_exp_per_year.get(student.year)
        if size == len(student.to_do): # this check if there is not scheduling at all
            output_excel.at[row_of_output, 'תעודת זהות'] = student.id_num
            output_excel.at[row_of_output, 'שם מלא'] = student.name
            output_excel.at[row_of_output, 'עיר מגורים'] = student.city
            output_excel.at[row_of_output, 'שנה'] = student.year
            output_excel.at[row_of_output, 'הערות'] = "בעיה - לא שובץ בכלום!"
        else:
            comment_in_excel = "לא שובץ ב: "
            for experience in student.to_do:
                comment_in_excel += experience + ","

            comment_in_excel = comment_in_excel[:-1]
            output_excel.at[row_of_output, 'הערות'] = comment_in_excel


# Experiences by years
second_year = ["ס.המבוגר - פנימית", "ס.המבוגר - כירורגית"]
third_year = ["טראומה מלרד - מיון", "סיעוד בקהילה", "ס.אישה - ס.אישה", "סיעוד בריאות הנפש", "ס.ילד - ילדים"]
fourth_year = ["סטאז"]  # Maybe will be deleted

num_of_exp_per_year = {'ב': 2, 'ג': 5, 'ד': 1, }

experience_by_year = {"B": second_year, "C": third_year, "D": fourth_year}

# -----------------------------------------------------------------

# A dict that holds KEY = City and VALUE = list of cities less than 50 km from the city in the KEY position.
cities_less_50_km_eng = {'Afula': ['Nahariyya', 'Afula', 'Zefat', 'Haifa', 'Pardesiya'],
                         'Ariel': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                   'Bnei Brak',
                                   'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Ashdod': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod', 'Bnei Brak',
                                    'Tel-Aviv', 'Hod Hasharon'], 'Ashkelon': ['Holon', 'Ashdod'],
                         'Arraba': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Baqa-Jatt': ['Kefar Sava', 'Petah Tikva', 'Raanana', 'Afula', 'Haifa', 'Ramat Gan',
                                       'Bnei Brak',
                                       'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Bat Yam': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                     'Bnei Brak',
                                     'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'], 'Beersheba': ["Be'er Sheva"],
                         "Beit She'an": ['Afula'],
                         'Beit Shemesh': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Ramat Gan', 'Ashdod',
                                          'Bnei Brak', 'Tel-Aviv', 'Hod Hasharon'],
                         'Baqa al-Gharbiyye': ['Kefar Sava', 'Petah Tikva', 'Raanana', 'Afula', 'Haifa', 'Ramat Gan',
                                               'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Beitar Illit': ['Jerusalem', 'Petah Tikva', 'Holon', 'Ramat Gan', 'Ashdod'],
                         'Bnei Brak': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                       'Ashdod',
                                       'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Dimona': ["Be'er Sheva"],
                         "El'ad": ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                   'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         "Giv'atayim": ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                        'Ashdod',
                                        'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         "Giv'at Shmuel": ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                           'Ashdod', 'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Hadera': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Afula', 'Haifa', 'Ramat Gan',
                                    'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Haifa': ['Nahariyya', 'Afula', 'Haifa'],
                         'Herzliya': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                      'Bnei Brak',
                                      'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Hod HaSharon': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                          'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Holon': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                   'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Jerusalem': ['Jerusalem', 'Petah Tikva', 'Holon', 'Ramat Gan', 'Bnei Brak'],
                         'Karmiel': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Kafr Qasim': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                        'Ashdod',
                                        'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Kfar Saba': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                       'Bnei Brak',
                                       'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Kiryat Ata': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Kiryat Bialik': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Kiryat Gat': ['Jerusalem', 'Holon', 'Ashdod', "Be'er Sheva"],
                         'Kiryat Malakhi': ['Jerusalem', 'Petah Tikva', 'Holon', 'Ramat Gan', 'Ashdod', 'Bnei Brak',
                                            'Tel-Aviv', 'Hod Hasharon'],
                         'Kiryat Motzkin': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Kiryat Ono': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                        'Ashdod',
                                        'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Kiryat Shmona': ['Zefat'], 'Kiryat Yam': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Lod': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                 'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         "Ma'ale Adumim": ['Jerusalem'], "Ma'alot-Tarshiha": ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Migdal HaEmek': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         "Modi'in Illit": ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                           'Ashdod', 'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         "Modi'in-Maccabim-Re'ut": ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana',
                                                    'Ramat Gan', 'Ashdod', 'Bnei Brak', 'Netanya', 'Tel-Aviv',
                                                    'Pardesiya',
                                                    'Hod Hasharon'], 'Maghar': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Nahariya': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Nazareth': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Nazareth Illit': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Nesher': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Ness Ziona': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                        'Ashdod',
                                        'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Netanya': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Bnei Brak',
                                     'Netanya',
                                     'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'], 'Netivot': ['Ashdod', "Be'er Sheva"],
                         'Ofakim': ["Be'er Sheva"],
                         'Or Akiva': ['Kefar Sava', 'Petah Tikva', 'Raanana', 'Afula', 'Haifa', 'Bnei Brak', 'Netanya',
                                      'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Or Yehuda': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                       'Ashdod',
                                       'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Nof HaGalil': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Petah Tikva': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                         'Ashdod', 'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Qalansawe': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Afula', 'Ramat Gan',
                                       'Bnei Brak',
                                       'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         "Ra'anana": ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                      'Bnei Brak',
                                      'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Rahat': ['Ashdod', "Be'er Sheva"],
                         'Ramat Gan': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                       'Ashdod',
                                       'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Ramat HaSharon': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                            'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Ramla': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                   'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Rehovot': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                     'Ashdod',
                                     'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Rishon LeZion': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                           'Ashdod', 'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Rosh HaAyin': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                         'Ashdod', 'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Safed': ['Nahariyya', 'Afula', 'Zefat'], 'Sakhnin': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Sderot': ['Ashdod', "Be'er Sheva"],
                         "Shefa-Amr (Shfar'am)": ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Tamra': ['Nahariyya', 'Afula', 'Zefat', 'Haifa'],
                         'Tayibe': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Afula', 'Ramat Gan', 'Bnei Brak',
                                    'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Tel Aviv': ['Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                      'Bnei Brak',
                                      'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Tiberias': ['Nahariyya', 'Afula', 'Zefat'],
                         'Tirat Carmel': ['Nahariyya', 'Afula', 'Haifa', 'Netanya'],
                         'Umm al-Fahm': ['Kefar Sava', 'Raanana', 'Afula', 'Haifa', 'Netanya', 'Pardesiya',
                                         'Hod Hasharon'],
                         'Yavne': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan', 'Ashdod',
                                   'Bnei Brak', 'Tel-Aviv', 'Hod Hasharon'],
                         'Yehud-Monosson': ['Jerusalem', 'Kefar Sava', 'Petah Tikva', 'Holon', 'Raanana', 'Ramat Gan',
                                            'Ashdod', 'Bnei Brak', 'Netanya', 'Tel-Aviv', 'Pardesiya', 'Hod Hasharon'],
                         'Yokneam': ['Nahariyya', 'Afula', 'Haifa', 'Netanya', 'Pardesiya']}

cities_less_50_km_heb = {'עפולה': ['נהריה', 'עפולה', 'צפת', 'חיפה', 'פרדסיה'],
                         'אריאל': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'בני ברק', 'נתניה',
                                   'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'אשדוד': ['כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                   'תל אביב-יפו', 'הוד השרון'], 'אשקלון': ['חולון', 'אשדוד'],
                         'עראבה': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         "באקה-ג'ת": ['כפר סבא', 'פתח תקווה', 'רעננה', 'עפולה', 'חיפה', 'רמת גן', 'בני ברק', 'נתניה',
                                      'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'בת ים': ['כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק', 'נתניה',
                                   'תל אביב-יפו', 'פרדסיה', 'הוד השרון'], 'באר שבע': ['באר שבע'], 'בית שאן': ['עפולה'],
                         'בית שמש': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רמת גן', 'אשדוד', 'בני ברק',
                                     'תל אביב-יפו', 'הוד השרון'],
                         'באקה אל-גרבייה': ['כפר סבא', 'פתח תקווה', 'רעננה', 'עפולה', 'חיפה', 'רמת גן', 'בני ברק',
                                            'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'ביתר עילית': ['ירושלים', 'פתח תקווה', 'חולון', 'רמת גן', 'אשדוד'],
                         'בני ברק': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                     'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'], 'דימונה': ['באר שבע'],
                         'אלעד': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                  'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'גבעתיים': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                     'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'גבעת שמואל': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד',
                                        'בני ברק', 'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'חדרה': ['כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'עפולה', 'חיפה', 'רמת גן', 'בני ברק',
                                  'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'], 'חיפה': ['נהריה', 'עפולה', 'חיפה'],
                         'הרצליה': ['כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק', 'נתניה',
                                    'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'כפר סבא': ['כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק', 'נתניה',
                                     'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'חולון': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                   'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'ירושלים': ['ירושלים', 'פתח תקווה', 'חולון', 'רמת גן', 'בני ברק'],
                         'כרמיאל': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'כפר קאסם': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                      'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'קריית אתא': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'קריית ביאליק': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'קריית גת': ['ירושלים', 'חולון', 'אשדוד', 'באר שבע'],
                         'קריית מלאכי': ['ירושלים', 'פתח תקווה', 'חולון', 'רמת גן', 'אשדוד', 'בני ברק', 'תל אביב-יפו',
                                         'הוד השרון'], 'קריית מוצקין': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'קריית אונו': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד',
                                        'בני ברק', 'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'קריית שמונה': ['צפת'], 'קריית ים': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'לוד': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                 'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'], 'מעלה אדומים': ['ירושלים'],
                         'מעלות תרשיחא': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'מגדל העמק': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'מודיעין עילית': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד',
                                           'בני ברק', 'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'מודיעין- מכבים- רעות': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן',
                                                  'אשדוד', 'בני ברק', 'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         "מע'אר": ['נהריה', 'עפולה', 'צפת', 'חיפה'], 'נצרת': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'נצרת עלית': ['נהריה', 'עפולה', 'צפת', 'חיפה'], 'נשר': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'נס ציונה': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                      'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'נתניה': ['כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'בני ברק', 'נתניה',
                                   'תל אביב-יפו', 'פרדסיה', 'הוד השרון'], 'נתיבות': ['אשדוד', 'באר שבע'],
                         'אופקים': ['באר שבע'],
                         'אור עקיבא': ['כפר סבא', 'פתח תקווה', 'רעננה', 'עפולה', 'חיפה', 'בני ברק', 'נתניה',
                                       'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'אור יהודה': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד',
                                       'בני ברק', 'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'נוף הגליל': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'פתח תקווה': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד',
                                       'בני ברק', 'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'קלנסווה': ['כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'עפולה', 'רמת גן', 'בני ברק', 'נתניה',
                                     'תל אביב-יפו', 'פרדסיה', 'הוד השרון'], 'רהט': ['אשדוד', 'באר שבע'],
                         'רמת גן': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                    'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'רמת השרון': ['כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק', 'נתניה',
                                       'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'רמלה': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                  'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'רחובות': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                    'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'ראשון לציון': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד',
                                         'בני ברק', 'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'ראש העין': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                      'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'סכנין': ['נהריה', 'עפולה', 'צפת', 'חיפה'], 'שדרות': ['אשדוד', 'באר שבע'],
                         'שפרעם': ['נהריה', 'עפולה', 'צפת', 'חיפה'], 'טמרה': ['נהריה', 'עפולה', 'צפת', 'חיפה'],
                         'טייבה': ['כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'עפולה', 'רמת גן', 'בני ברק', 'נתניה',
                                   'תל אביב-יפו', 'פרדסיה', 'הוד השרון'], 'טבריה': ['נהריה', 'עפולה', 'צפת'],
                         'טירת כרמל': ['נהריה', 'עפולה', 'חיפה', 'נתניה'],
                         'אום אל-פחם': ['כפר סבא', 'רעננה', 'עפולה', 'חיפה', 'נתניה', 'פרדסיה', 'הוד השרון'],
                         'יבנה': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד', 'בני ברק',
                                  'תל אביב-יפו', 'הוד השרון'],
                         'יהוד-מונסון': ['ירושלים', 'כפר סבא', 'פתח תקווה', 'חולון', 'רעננה', 'רמת גן', 'אשדוד',
                                         'בני ברק', 'נתניה', 'תל אביב-יפו', 'פרדסיה', 'הוד השרון'],
                         'יקנעם עילית': ['נהריה', 'עפולה', 'חיפה', 'נתניה', 'פרדסיה']}

# ------------------------------------------------------------------

cities_with_hospitals_h_e = {"ירושלים": "Jerusalem", "נהריה": "Nahariyya", "כפר סבא": "Kefar Sava",
                             "פתח תקווה": "Petah Tikva", "חולון": "Holon", "רעננה": "Raanana", "עפולה": "Afula",
                             "צפת": "Zefat", "חיפה": "Haifa", "רמת גן": "Ramat Gan", "אשדוד": "Ashdod",
                             "בני ברק": "Bnei Brak", "נתניה": "Netanya", "תל אביב": "Tel-Aviv", "פרדסיה": "Pardesiya",
                             "באר שבע": "Be'er Sheva", "הוד השרון": "Hod Hasharon"}

cities_with_hospitals_e_h = {'Jerusalem': 'ירושלים', 'Nahariyya': 'נהריה', 'Kefar Sava': 'כפר סבא',
                             'Petah Tikva': 'פתח תקווה',
                             'Holon': 'חולון', 'Raanana': 'רעננה', 'Afula': 'עפולה', 'Zefat': 'צפת', 'Haifa': 'חיפה',
                             'Ramat Gan': 'רמת גן',
                             'Ashdod': 'אשדוד', 'Bnei Brak': 'בני ברק', 'Netanya': 'נתניה', 'Tel-Aviv': 'תל אביב',
                             'Pardesiya': 'פרדסיה',
                             "Be'er Sheva": 'באר שבע', 'Hod Hasharon': 'הוד השרון'}

# Maybe not necessary
hospitals = ["שערי צדק", "הדסה עין כרם", "הדסה הר צופים", "המרכז הרפואי הרצוג", "בית חולים נהריה", "בית חולים מאיר",
             "לניאדו", "השרון", "בלינסון", "שיבא תל השומר", "וולפסון", "אסותא אשדוד", "אסותא רמת החייל", "דורות",
             "בית רבקה", "מעייני הישועה", "בית לוינשטין", "זיו", "העמק", "רמב'ם", "כרמל", "סורוקה", "פרדסיה לב השרון",
             "גהה", "שלוותא", "כפר שאול", "נפש באר שבע"]

# -----------------------------------------------------------------
# One dict that holds all the cities in israel, KEY = city_english , VALUE = city_hebrew
# And the second dict that holds all the cities in israel, KEY = city_hebrew , VALUE = city_english

cities_in_israel_en_heb = {'Afula': 'עפולה', 'Arad': 'ערד', 'Ariel': 'אריאל', 'Ashdod': 'אשדוד', 'Ashkelon': 'אשקלון',
                           'Arraba': 'עראבה',
                           'Baqa-Jatt': "באקה-ג'ת", 'Bat Yam': 'בת ים', 'Beersheba': 'באר שבע',
                           "Beit She'an": 'בית שאן',
                           'Beit Shemesh': 'בית שמש', 'Baqa al-Gharbiyye': 'באקה אל-גרבייה',
                           'Beitar Illit': 'ביתר עילית', 'Bnei Brak': 'בני ברק',
                           'Dimona': 'דימונה', 'Eilat': 'אילת', "El'ad": 'אלעד', "Giv'atayim": 'גבעתיים',
                           "Giv'at Shmuel": 'גבעת שמואל',
                           'Hadera': 'חדרה', 'Haifa': 'חיפה', 'Herzliya': 'הרצליה', 'Hod HaSharon': 'הוד השרון',
                           'Holon': 'חולון',
                           'Jerusalem': 'ירושלים', 'Karmiel': 'כרמיאל', 'Kafr Qasim': 'כפר קאסם',
                           'Kfar Saba': 'כפר סבא',
                           'Kiryat Ata': 'קריית אתא', 'Kiryat Bialik': 'קריית ביאליק', 'Kiryat Gat': 'קריית גת',
                           'Kiryat Malakhi': 'קריית מלאכי',
                           'Kiryat Motzkin': 'קריית מוצקין', 'Kiryat Ono': 'קריית אונו', 'Kiryat Shmona': 'קריית שמונה',
                           'Kiryat Yam': 'קריית ים',
                           'Lod': 'לוד', "Ma'ale Adumim": 'מעלה אדומים', "Ma'alot-Tarshiha": 'מעלות תרשיחא',
                           'Migdal HaEmek': 'מגדל העמק',
                           "Modi'in Illit": 'מודיעין עילית', "Modi'in-Maccabim-Re'ut": 'מודיעין- מכבים- רעות',
                           'Maghar': "מע'אר",
                           'Nahariya': 'נהריה', 'Nazareth': 'נצרת', 'Nazareth Illit': 'נצרת עלית', 'Nesher': 'נשר',
                           'Ness Ziona': 'נס ציונה',
                           'Netanya': 'נתניה', 'Netivot': 'נתיבות', 'Ofakim': 'אופקים', 'Or Akiva': 'אור עקיבא',
                           'Or Yehuda': 'אור יהודה',
                           'Nof HaGalil': 'נוף הגליל', 'Petah Tikva': 'פתח תקווה', 'Qalansawe': 'קלנסווה',
                           "Ra'anana": 'רעננה', 'Rahat': 'רהט',
                           'Ramat Gan': 'רמת גן', 'Ramat HaSharon': 'רמת השרון', 'Ramla': 'רמלה', 'Rehovot': 'רחובות',
                           'Rishon LeZion': 'ראשון לציון', 'Rosh HaAyin': 'ראש העין', 'Safed': 'צפת',
                           'Sakhnin': 'סכנין', 'Sderot': 'שדרות',
                           "Shefa-Amr (Shfar'am)": 'שפרעם', 'Tamra': 'טמרה', 'Tayibe': 'טייבה',
                           'Tel Aviv': 'תל אביב-יפו', 'Tiberias': 'טבריה',
                           'Tira': 'טירה', 'Tirat Carmel': 'טירת כרמל', 'Umm al-Fahm': 'אום אל-פחם', 'Yavne': 'יבנה',
                           'Yehud-Monosson': 'יהוד-מונסון', 'Yokneam': 'יקנעם עילית'}

cities_in_israel_heb_eng = {'עפולה': 'Afula', 'ערד': 'Arad', 'אריאל': 'Ariel', 'אשדוד': 'Ashdod', 'אשקלון': 'Ashkelon',
                            'עראבה': 'Arraba',
                            "באקה-ג'ת": 'Baqa-Jatt', 'בת ים': 'Bat Yam', 'באר שבע': 'Beersheba',
                            'בית שאן': "Beit She'an",
                            'בית שמש': 'Beit Shemesh', 'באקה אל-גרבייה': 'Baqa al-Gharbiyye',
                            'ביתר עילית': 'Beitar Illit',
                            'בני ברק': 'Bnei Brak', 'דימונה': 'Dimona', 'אילת': 'Eilat', 'אלעד': "El'ad",
                            'גבעתיים': "Giv'atayim",
                            'גבעת שמואל': "Giv'at Shmuel", 'חדרה': 'Hadera', 'חיפה': 'Haifa', 'הרצליה': 'Herzliya',
                            'הוד השרון': 'Hod HaSharon', 'חולון': 'Holon', 'ירושלים': 'Jerusalem', 'כרמיאל': 'Karmiel',
                            'כפר קאסם': 'Kafr Qasim', 'כפר סבא': 'Kfar Saba', 'קריית אתא': 'Kiryat Ata',
                            'קריית ביאליק': 'Kiryat Bialik',
                            'קריית גת': 'Kiryat Gat', 'קריית מלאכי': 'Kiryat Malakhi', 'קריית מוצקין': 'Kiryat Motzkin',
                            'קריית אונו': 'Kiryat Ono', 'קריית שמונה': 'Kiryat Shmona', 'קריית ים': 'Kiryat Yam',
                            'לוד': 'Lod',
                            'מעלה אדומים': "Ma'ale Adumim", 'מעלות תרשיחא': "Ma'alot-Tarshiha",
                            'מגדל העמק': 'Migdal HaEmek',
                            'מודיעין עילית': "Modi'in Illit", 'מודיעין- מכבים- רעות': "Modi'in-Maccabim-Re'ut",
                            "מע'אר": 'Maghar',
                            'נהריה': 'Nahariya', 'נצרת': 'Nazareth', 'נצרת עלית': 'Nazareth Illit', 'נשר': 'Nesher',
                            'נס ציונה': 'Ness Ziona',
                            'נתניה': 'Netanya', 'נתיבות': 'Netivot', 'אופקים': 'Ofakim', 'אור עקיבא': 'Or Akiva',
                            'אור יהודה': 'Or Yehuda',
                            'נוף הגליל': 'Nof HaGalil', 'פתח תקווה': 'Petah Tikva', 'קלנסווה': 'Qalansawe',
                            'רעננה': "Ra'anana",
                            'רהט': 'Rahat', 'רמת גן': 'Ramat Gan', 'רמת השרון': 'Ramat HaSharon', 'רמלה': 'Ramla',
                            'רחובות': 'Rehovot',
                            'ראשון לציון': 'Rishon LeZion', 'ראש העין': 'Rosh HaAyin', 'צפת': 'Safed',
                            'סכנין': 'Sakhnin', 'שדרות': 'Sderot',
                            'שפרעם': "Shefa-Amr (Shfar'am)", 'טמרה': 'Tamra', 'טייבה': 'Tayibe',
                            'תל אביב-יפו': 'Tel Aviv',
                            'טבריה': 'Tiberias', 'טירה': 'Tira', 'טירת כרמל': 'Tirat Carmel',
                            'אום אל-פחם': 'Umm al-Fahm', 'יבנה': 'Yavne',
                            'יהוד-מונסון': 'Yehud-Monosson', 'יקנעם עילית': 'Yokneam'}

# -----------------------------------------------------------------

# Read the excel of the Students to get the length of his rows and column
students_excel = pandas.read_excel('students.xlsx')
n_rows_student = len(students_excel.index)
n_cols_student = len(students_excel.columns)

# students is a list that contain elements of student object
students = create_list_students()

# -----------------------------------------------------------------

# Create an Output Excel

data = {'תעודת זהות': [], 'שם מלא': [], 'שנה': [], 'עיר מגורים': [], 'התנסות א': [], 'בית חולים א': [], 'תאריכים א': [],
     'התנסות ב': [], 'בית חולים ב': [], 'תאריכים ב': [], 'התנסות ג': [], 'בית חולים ג': [], 'תאריכים ג': [],
     'התנסות ד': [], 'בית חולים ד': [], 'תאריכים ד': [], 'התנסות ה': [], 'בית חולים ה': [], 'תאריכים ה': [], 'הערות': [] }

output_excel = pandas.DataFrame(data)

# Read the excel of the Hospitals to get the length of his rows and column
hospitals_excel = pandas.read_excel("Hospitals.xlsx")
n_rows_hospital = len(hospitals_excel.index)
n_cols_hospital = len(hospitals_excel.columns)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pandas.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
output_excel.to_excel(writer, sheet_name='Sheet1', index=False)

row_of_output = 1  # when we finish with a student we add 1


for s in students:

    num_of_experience = 0  # start from zero until the length of the to do list in student object
    for row in range(n_rows_hospital):
        city_host = str(hospitals_excel.iloc[row][0])  # city of the experience
        student_num = hospitals_excel.iloc[row][4]
        experience_host = hospitals_excel.iloc[row][2] + " - " + hospitals_excel.iloc[row][3]
        hospital = hospitals_excel.iloc[row][1]
        dates = hospitals_excel.iloc[row][6]

        if city_host in s.list_of_potential_cities:

            if experience_host in s.to_do:

                if student_num > 0:
                    print(f" id num is : {s.id_num}")
                    print(f" the list exp is: {s.to_do}")
                    flag = False
                    #hospitals_excel.at[row, 'מספר סטודנטים'] = student_num - 1
                    # hospitals_excel.to_excel("Hospitals.xlsx", index=False)
                    output_excel.at[row_of_output, 'תעודת זהות'] = s.id_num
                    output_excel.at[row_of_output, 'שם מלא'] = s.name
                    output_excel.at[row_of_output, 'עיר מגורים'] = s.city
                    output_excel.at[row_of_output, 'שנה'] = s.year

                    if num_of_experience == 0:
                        output_excel.at[row_of_output, 'התנסות א'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים א'] = hospital
                        output_excel.at[row_of_output, 'תאריכים א'] = dates
                        flag = True

                    elif num_of_experience == 1:
                        output_excel.at[row_of_output, 'התנסות ב'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים ב'] = hospital
                        output_excel.at[row_of_output, 'תאריכים ב'] = dates
                        flag = True

                    elif num_of_experience == 2:
                        output_excel.at[row_of_output, 'התנסות ג'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים ג'] = hospital
                        output_excel.at[row_of_output, 'תאריכים ג'] = dates
                        flag = True

                    elif num_of_experience == 3:
                        output_excel.at[row_of_output, 'התנסות ד'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים ד'] = hospital
                        output_excel.at[row_of_output, 'תאריכים ד'] = dates
                        flag = True

                    else:
                        output_excel.at[row_of_output, 'התנסות ה'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים ה'] = hospital
                        output_excel.at[row_of_output, 'תאריכים ה'] = dates
                        flag = True

                    if flag:
                        num_of_experience += 1
                        s.done.append(experience_host)
                        # print(f"id num : {s.id_num}")
                        # print(f" the list is : {s.to_do}")
                        temp = []
                        for exp in s.to_do:
                            if exp != experience_host:
                                temp.append(exp)
                        s.to_do = temp

    #
    write_comment(s)
    row_of_output += 1

output_excel.style.background_gradient(cmap='Greens')


# Close the Pandas Excel writer and output the Excel file.
# output_excel.at[i, 'תעודת זהות'] = 207935214
# print(output_excel.at[i, 'תעודת זהות'])
# print(output_excel)
# writer.save()
output_excel.to_excel("Demo.xlsx", index=False)

# start to Scheduling
