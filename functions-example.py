# python3 functions cannot have dashes/hiphens in their names
# but dictionary keys can have dashes in key names
#
students = []

def printNames():
    student_list = get_students()
    # print each student
    for student in students:
        print(student)

def get_students():
    return students

def add_student(fname,mi,lname,std_id):
    # create student object
    student = {"name": fname+" "+mi+" "+lname, "student-id":std_id}
    # adding to global var students
    students.append(student)

def var_args(name, *args):
    print(name)
    #print(args)

add_student("Raja","C","Bangaru",326)
var_args("Ivaan", "Vijay","Bangaru", 6 ,"years old.")
printNames()


