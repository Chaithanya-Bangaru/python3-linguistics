# dictionary type is like JSON datatype
tuple = ["raja",1,"bangaru"]
#set set is like distinct elements but also they are ordered
#frozenset
print(tuple)

student = {
    "student_id": "99391A0326",
    "first_name": "Raja",
    "last_name": "Bangaru",
    "state_code": "NE",
    "city": "Omaha"
}
try:
    student["middle_name"] = "Chaithanya"
    #number_of_sisters = student["middle_name"] + 4
    #print("Input a number")
    numb = int(input("\nPlease enter a number:"))
    print("you entered",numb)
except TypeError as typeerror:
    print("TypeError!")
    print(typeerror)
except KeyError as keyerror:
    print("KeyError occured!")
except ValueError as valueerror:
    print("ValueError occured!")
# except Exception as exception:
#     print("Unknown Exception!",exception)
finally:
    print("This finally code still executes..")
