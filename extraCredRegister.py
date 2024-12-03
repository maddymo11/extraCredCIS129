#register for class schedule
# class title, class days, class time
#print out schedule at the end

# Madison Simonds
# Mei Li Chan
# Amy Cardona

#welcome message
print('Welcome to Pima Community College')
print('Class registration is open now!')

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
    
    printSchedule(firstName, lastName, studentID) #pass values to print function

    return firstName, lastName, studentID
#now that we have student info, go to class registration

#blah blah blah


#lastly, display schedule to user 
def printSchedule(firstName, lastName, studentID):
    print('*' * 36)
    print(f'{firstName} {lastName} \nStudent ID: {studentID}')
main()

    