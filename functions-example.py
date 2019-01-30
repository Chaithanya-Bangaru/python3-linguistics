# python3 functions cannot have dashes/hiphens in their names
# but dictionary keys can have dashes in key names
#
students = []

def printNames():
    student_list = get_students()
    # print each student
    for student in students:
        print(student,"\n")

def get_students():
    return students

def add_student(fname,mi,lname,std_id):
    # create student object
    student = {"name": fname+" "+mi+" "+lname, "student-id":std_id}
    # adding to global var students
    students.append(student)

def var_args(name, *args):
    print(name)
    print(args,"\n")

def keyword_args_func(firstname, **kwargs):
    print(firstname,"\n")
    print(kwargs["lastname"],"\n")
    print(kwargs["lastname"],"\n")
    print(kwargs["lastname"],"\n")

def keyword_args_func2(firstname, **kwargs):
        print(firstname)
        print(kwargs["lastname"], "\n")

printNames()

add_student("Raja","C","Bangaru",326)
var_args("Ivaan", "Vijay","Bangaru", 6 ,"years old.")
keyword_args_func(firstname="Ivaan", mi="Vijay",lastname="Bangaru", age=6 ,comment="years old.")

keyword_args_func2(firstname="Ivaan", mi="Vijay",lastname="Bangaru", age=6 ,comment="years old.")


