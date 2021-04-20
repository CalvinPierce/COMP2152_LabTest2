# Question 1
import csv

file = 'student.csv'


# Reading
def readData():
    print("Student First Name \t Student Last Name \t Grade")
    with open(file, 'r') as my_file:
        reader = csv.reader(my_file)
        sum_csv = 0
        count = 0
        for row in reader:
            print("\t\t\t\t".join(row))
            sum_csv = sum_csv + int(row[2])
            count = count + 1

    print("\n")
    print("Grade average: ", int(sum_csv / count))
    my_file.close()


# Writing
def writeData():
    fullName = input("Please enter the student name separated by a space: ")
    firstName, lastName = fullName.split(" ")
    grade = input("Please enter a grade: ")
    data = [firstName, lastName, grade]
    with open(file, 'a') as my_file:
        writer = csv.writer(my_file, lineterminator='\n')
        writer.writerow(data)
        my_file.close()


def menu():
    print("\n")
    print("Welcome to Calvin's Lab Test 2!")
    print("1) View students")
    print("2) Add student")
    print("3) Exit")


option = 0
while option != 3:
    menu()
    option = int(input("Please select an option from the menu"))
    if option == 1:
        readData()
    elif option == 2:
        writeData()
    elif option == 3:
        print("Goodbye")
        break
    else:
        print("Option not valid!")
