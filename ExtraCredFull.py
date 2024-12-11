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


#register for course by CRN
def searchByCRN(file_path, studentClasses):
    #studentClasses = [] #empty list to add registered classes
    while True:
        pickCRN = input('Please enter the CRN of the course you will be registering for. (type exit to stop)\n')
        if pickCRN.lower() == 'exit':
            print('Exiting registration...')
            break

        with open(file_path, mode='r') as classFile:
            reader = csv.DictReader(classFile)
            courseFound = False #flag to check CRN

                #loop through rows
            for row in reader:
                if row["CRN"] == pickCRN:
                    print(f'You have registered for {row["Class"]}, {row["SubjectCode"]}{row["CourseNumber"]}.')
                    courseFound = True
                    while True:
                        confirmReg = input('Is this correct? Enter y or n.\n')
                        if confirmReg == 'n':
                            print('Restarting search...')
                            break
                        elif confirmReg == 'y':
                            print('Adding class to your schedule...')
                            studentClasses.append({
                                'Class': row["Class"],
                                'SubjectCode': row["SubjectCode"],
                                'CourseNumber': row["CourseNumber"],
                                'CRN': row["CRN"]
                            })
                            print(f'{row["Class"]} has been aded to your schedule.')
                            break
                        else:
                            print('Invalid input. Please enter y or n.')

            if not courseFound:
                print('No class found with provided CRN.')


                    
        moreCourses = input('Would you like to register for another course? Enter y or n.\n')
        if moreCourses.lower() == 'n':
            break
        elif moreCourses.lower() != 'y':
            print('Invalid Input. Please enter y or n.')



#prompt to choose course
def chooseCourse(file_path, firstName, lastName, studentID):
    studentClasses = []
    while True:
        matchingRow = [] #list to store relevant courses
        with open(file_path, mode='r') as classFile:
            reader = csv.DictReader(classFile)
            print('Here are the available subjects for registration:') #print available subjects
            print('Math, Science, Literature, Arts, Language, History, Technology, Engineering')

            #get subject request
            rawRequest = input("Please enter the subject of the class you are interested in. Enter 'exit' to stop. \n")
            #validate input
            stripRequest = rawRequest.strip()
            if not stripRequest.isalpha():
                print('Invalid. Classes cannot contain digits.')
                continue
            lowerRequest = stripRequest.lower()
            if lowerRequest == 'exit':
                print('Exiting...')
                break
            subjectRequest = lowerRequest.capitalize()

            #loop through rows to list subject information
            for row in reader:
                if row["Subject"] == subjectRequest:
                    matchingRow.append(row) #add each matching subject to list of info
        
            #if no matches are found, print class not found
            if not matchingRow:
                print('Class Not Found')
                continue

            #if matches are found, display them
            for row in matchingRow:
                print(f'Subject Information: ({row["SubjectCode"]}{row["CourseNumber"]}) {row["Class"]}, CRN: {row["CRN"]}')
    
        searchByCRN(file_path, studentClasses)
        #ask if user wants more courses
        moreSubjects = input('Would you like to search for another subject? Enter y or n.\n')
        if moreSubjects.lower() == 'n':
            print('Exiting...')
            break
        elif moreSubjects.lower() != 'y':
            print('Invalid input. Please enter y or n.')    #FIX LOOP TO VALIDATE INPUT
        break
    
    return studentClasses



#display schedule to user 
def printSchedule(firstName, lastName, studentID, studentClasses):
    print('*' * 36)
    print(f'{firstName} {lastName} \nStudent ID: {studentID}')
    print('Class Schedule:')
    for course in studentClasses:
        print(f"{course['SubjectCode']}{course['CourseNumber']} - {course['Class']} (CRN: {course['CRN']})")





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
    studentClasses = chooseCourse(file_path, firstName, lastName, studentID)
    
    printSchedule(firstName, lastName, studentID, studentClasses) #pass values to print function

    #return firstName, lastName, studentID

main()

