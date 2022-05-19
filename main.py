import pandas
import pandas as pd
import openpyxl
from xlsxwriter import Workbook
from Student import Student
from geopy.geocoders import Nominatim
from geopy import distance

## hospitals = ["ירושלים", "כפר סבא", "נתניה", "פתח תקווה", "רמת גן", "אשדוד", "חולון", "תל אביב", "בני ברק",
#               "רעננה", "עפולה", "צפת", "חיפה", "באר שבע"]

# soul = ["פרדסיה לב השרון ?", "פתח תקווה", "הוד השרון", "כפר סבא", "באר שבע"]

def create_list_students(n_row: int, n_cols: int, excel) -> list:
    students_object = []

    for row in range(10): # change to 10 for check should be row
        experience_lst = []
        flag_year = True
        id_num = students_excel.iloc[row][0]
        full_name = students_excel.iloc[row][1] + " " + students_excel.iloc[row][2]
        year = students_excel.iloc[row][5]
        city = students_excel.iloc[row][6]

        if year == 'א':
            flag_year = False

        elif year == 'ב':
            experience_lst = experience_by_year.get("B")

        elif year == 'ג':
            experience_lst = experience_by_year.get("C")

        else:
            experience_lst = experience_by_year.get("D")

        if flag_year:
            list_of_potential_cities = create_list_potential_cities(city)
            #list_of_potential_cities = []
            #print(list_of_potential_cities)
            #print(city)
            student = Student(id_num, full_name, city, year, experience_lst, list_of_potential_cities)
            students_object.append(student)

    return students_object


def find_distance_between_cities(c1, c2):
    geolocatar = Nominatim(user_agent="geoapiExercises")

    # These variables have the exact location of the cities
    l1 = geolocatar.geocode(c1)
    l2 = geolocatar.geocode(c2)

    loc1 = (l1.latitude, l1.longitude)
    loc2 = (l2.latitude, l2.longitude)

    dist_in_km = round(distance.distance(loc1, loc2).km)
    return dist_in_km


def create_list_potential_cities(city: str) -> list:
    list_of_potential_cities = []
    for city_with_host in cities_with_hospitals:
        dist_km = find_distance_between_cities(city, city_with_host)
        if dist_km <= 45:
            list_of_potential_cities.append(city_with_host)

    return list_of_potential_cities


def Experience_distribution():
    pass


experience_by_year = {"B": ["ס. המבוגר - פנימית", "ס. המבוגר - כירורגית"],
                      "C": ["טראומה מלרד/מיון", "סיעוד הקהילה", "ס. האישה - ס. האישה", "סיעוד בריאות הנפש", "ס. הילד - ילדים"],
                      "D": ["סטאז"]}

# read the excel of the Students to get the length of it
students_excel = pandas.read_excel('students.xlsx')
n_rows = len(students_excel.index)
n_cols = len(students_excel.columns)

cities_with_hospitals = {"נתניה": "Netanya", "תל אביב": "Tel-Aviv", "כפר סבא": "Kfar Saba", "פתח תקווה": "Petah Tiqwa",
                            "רמת גן": "Ramat Gan", "אשדוד": "Ashdod", "חולון": "Holon", "בני ברק": "Bnei Brak",
                            "רעננה": "Raanana", "עפולה": "Afula", "צפת": "Zefat", "חיפה": "Haifa", "ירושלים": "Jerusalem"
                         }


# students is a list that contain elements of student object
students = create_list_students(n_rows, n_cols, students_excel)

# read the excel of the Hospitals to get the length of it
hospitals_excel = pandas.read_excel("Hospitals.xlsx")
n_rows = len(hospitals_excel.index)
n_cols = len(hospitals_excel.columns)


# dataframe Name and Age columns
output_excel = pd.DataFrame({'תעודת זהות':[], 'שם מלא':[], 'שנה':[], 'עיר מגורים':[], 'התנסות א':[], 'בית חולים א':[], 'תאריכים א':[],
                   'התנסות ב': [], 'בית חולים ב': [], 'תאריכים ב': [], 'התנסות ג':[], 'בית חולים ג':[], 'תאריכים ג':[],
                   'התנסות ד': [], 'בית חולים ד': [], 'תאריכים ד': [], 'התנסות ה':[], 'בית חולים ה':[], 'תאריכים ה':[],
                             })

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
output_excel.to_excel(writer, sheet_name='Sheet1', index=False)

row_of_output = 1

for s in students:
    num_of_experience = 0
    for row in range(n_rows):
        city_host = hospitals_excel.iloc[row][0]
        student_num = hospitals_excel.iloc[row][4]
        experience_host = hospitals_excel.iloc[row][2] + " - " + hospitals_excel.iloc[row][3]
        hospital = hospitals_excel.iloc[row][1]
        dates = hospitals_excel.iloc[row][6]


        if city_host in s.list_of_potential_cities:
            print("experience is : " + experience_host)
            print("and to do is :")
            print(s.to_do)
            if experience_host in s.to_do:
                print("entered secound if")
                if student_num > 0:
                    print("entered last if")
                    hospitals_excel.at[row, 'מספר סטודנטים'] = student_num - 1
                    #hospitals_excel.to_excel("Hospitals.xlsx", index=False)
                    output_excel.at[row_of_output, 'תעודת זהות'] = s.id_num
                    output_excel.at[row_of_output, 'שם מלא'] = s.name
                    output_excel.at[row_of_output, 'עיר מגורים'] = s.city
                    output_excel.at[row_of_output, 'שנה'] = s.year

                    if num_of_experience == 0:
                        output_excel.at[row_of_output, 'התנסות א'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים א'] = hospital
                        output_excel.at[row_of_output, 'תאריכים א'] = dates

                    elif num_of_experience == 1:
                        output_excel.at[row_of_output, 'התנסות ב'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים ב'] = hospital
                        output_excel.at[row_of_output, 'תאריכים ב'] = dates

                    elif num_of_experience == 2:
                        output_excel.at[row_of_output, 'התנסות ג'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים ג'] = hospital
                        output_excel.at[row_of_output, 'תאריכים ג'] = dates

                    elif num_of_experience == 3:
                        output_excel.at[row_of_output, 'התנסות ד'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים ד'] = hospital
                        output_excel.at[row_of_output, 'תאריכים ד'] = dates

                    else:
                        output_excel.at[row_of_output, 'התנסות ה'] = experience_host
                        output_excel.at[row_of_output, 'בית חולים ה'] = hospital
                        output_excel.at[row_of_output, 'תאריכים ה'] = dates

                    num_of_experience = num_of_experience + 1

    row_of_output = row_of_output + 1




# Close the Pandas Excel writer and output the Excel file.
# output_excel.at[i, 'תעודת זהות'] = 207935214
# print(output_excel.at[i, 'תעודת זהות'])
print(output_excel)
# writer.save()
output_excel.to_excel("Demo.xlsx", index = False)

# start to Scheduling

