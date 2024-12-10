#register for class schedule
# class title, class days, class time
#print out schedule at the end

# Madison Simonds
# Mei Li Chan
# Amy Cardona

#welcome message
print('Welcome to Pima Community College')
print('Class registration is open now!')

import csv #import file for classes

#register for courses
def chooseCourse(file_path):
    while True:
        matchingRow = [] #list to store relevant courses
        with open(file_path, mode='r') as classFile:
            reader = csv.DictReader(classFile)
            subjectRequest = input('Please enter the subject of the class you are interested in.\n')


        #loop through rows to list subject information
            for row in reader:
                if row["Subject"] == subjectRequest:
                    matchingRow.append(row) #add each matching subject to list of info
        
        #if no matches are found, print class not found
            if not matchingRow:
                return 'Class Not Found'

        #if matches are found, display them
            for row in matchingRow:
                print(f'Subject Information: ({row["SubjectCode"]}{row["CourseNumber"]}) {row["Class"]}, CRN: {row["CRN"]}')
            
            #loop to add more courses
            moreCourses = input('Would you like to register for another course? Enter y or n.\n')
            if moreCourses == 'n':
                break
            elif moreCourses == 'y':
                continue
            else:
                print('Invalid Input. Please enter y or n.')



#lastly, display schedule to user 
def printSchedule(firstName, lastName, studentID):
    print('*' * 36)
    print(f'{firstName} {lastName} \nStudent ID: {studentID}')
    print('Class Schedule:')


#main to get student info
def main():
    #loop to get ID
    while True:
        studentID = input('To begin, please enter your Student ID number. (type exit to stop)\n')
        #check if user entered exit
        if studentID.lower() == 'exit':
            print('Exiting Registration.')
            return
        #validate input is digit
        elif not studentID.isdigit():
            print('Invalid. Your Student ID must be a number.')
            continue
        #move on if input is OK
        elif studentID.isdigit():
            break

    #loops to get student Name
    while True:
        #get first name
        firstName = input('Please enter your first name.\n')
        if not firstName.isalpha(): #make sure name is only letters
            print('You must enter a name. Please Try Again.')
            continue
        elif firstName.isalpha():
            break
    while True:
        #get last name
        lastName = input('Please enter your last name.\n')
        if not lastName.isalpha(): #make sure name is only letters
            print('You must enter a name. Please Try Again.')
            continue
        elif lastName.isalpha():
            break

        
    #call chooseCourse to select courses
    file_path = 'allClasses.csv'
    result = chooseCourse(file_path)

    if result == 'Class Not Found':
        print(result)
    elif result == None:
        print('You did not register for any classes.')
    else: 
        print('You have registered for the following courses:\n')
        for row in result:
            print(f'Subject Information: ({row["SubjectCode"]}{row["CourseNumber"]}) {row["Class"]}, CRN: {row["CRN"]}')

    printSchedule(firstName, lastName, studentID) #pass values to print function

    return firstName, lastName, studentID


main()