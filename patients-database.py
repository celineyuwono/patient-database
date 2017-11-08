__author__ = 'Celine Yuwono, yuwono@live.unc.edu, Onyen = yuwono'

# Variables that has the name containing a loop (ex loopy, loop_loop) is a loop!

def menu():
    # Define global variable
    global patient_study_file_name
    # PAGE 267-269 Temporary Files
    # Ask user for file name (must be valid file)
    patient_study_file_name = input('Please Enter Patient-Study FileName: ')
    # Loop if user insert invalid file name
    loop = True
    while loop:
        try:
            # Validate file
            file = open(patient_study_file_name,'r')
            file.close()
            clean_spaces()
            # Break loop
            break
        except IOError:
            print('File does not exist.')
            patient_study_file_name = input('Please Enter a Valid Patient-Study FileName: ')
            clean_spaces()

    loopy = True
    while loopy:
        # MENU ITEMS
        print('Menu')
        print('WARNING! This program is case-sensitive.')
        print('1. Add Patient Record')
        print('2. Delete a Patient Record')
        print('3. Count Number of Patients in a Specific Study')
        print('4. Display Patients in a Specific Study')
        print('5. Display All Patient Record')
        print('6. Display Number of Patients for All Study')
        print('7. Search Patient Record by Patient Name')
        print('8. Quit')
        # Clean record
        clean_spaces()

        # Prompt user input (number between 1-6)
        user_input = int(input('Enter your choice number (1-6): '))

        # Go to specific function based on user's choice
        if(user_input == 1):
            add_patient_record()
        if(user_input == 2):
            delete_patient_record()
        if(user_input == 3):
            count_patient_in_study()
        if(user_input == 4):
            display_patient_in_study()
        if(user_input == 5):
            display_patient_record()
        if(user_input == 6):
            tally_patients_by_study()
        if(user_input == 7):
            search_patient()
        if(user_input == 8):
            pass
        back_or_exit = input('\n1. Back to menu\n2. Quit\nChoose 1 or 2: ')
        # If user choose to go back to the menu
        if back_or_exit == '1':
            clean_spaces()
            continue
        # If user choose to exit program.
        elif back_or_exit == '2':
            clean_spaces()
            break
        else:
            while back_or_exit != '1' and back_or_exit != '2':
                print('Please choose either 1 or 2! ')
                back_or_exit = input('\n1. Back to menu\n2. Quit\nChoose 1 or 2: ')
            if back_or_exit == '2':
                break
        continue

def clean_spaces():
    global patient_study_file_name
    import os
    # Erase all blank spaces between patient record

    clean_lines = []
    with open(patient_study_file_name, 'r') as f:
        lines = f.readlines()
        clean_lines = [l.strip() for l in lines if l.strip()]

    with open('test2.txt', 'w') as f:
        f.writelines('\n'.join(clean_lines))

    os.remove(patient_study_file_name)
    os.rename('test2.txt', patient_study_file_name)

    # Add 1 space between every patient record
    readfile = open(patient_study_file_name, 'r')
    writefile = open('test2.txt', 'w')

    # Prompt readline
    read_name = readfile.readline()
    read_age = readfile.readline()
    read_study = readfile.readline()

    while read_name != '' and read_age != '':
        # Strip line
        read_name = read_name.rstrip()
        read_age = read_age.rstrip()
        read_study = read_study.rstrip()

        # Write files
        writefile.write(str(read_name) + '\n')
        writefile.write(str(read_age) + '\n')
        writefile.write(str(read_study) + '\n\n')

        # Loop
        read_name = readfile.readline()
        read_age = readfile.readline()
        read_study = readfile.readline()

    # Close files
    readfile.close()
    writefile.close()

    # Replace files
    os.remove(patient_study_file_name)
    os.rename('test2.txt', patient_study_file_name)

def add_patient_record():
    # Define global variable
    global patient_study_file_name
    # While user wants to input additional patient record
    add_additional_patient_record = 'y'
    while(add_additional_patient_record == 'y'):
        # While user input is invalid, there will be a loop
        need_to_loop = True
        while need_to_loop:
            try:
                # Prompt user input
                patient_name = input('Patient name: ')
                patient_age = input('Patient age: ')
                patient_study = input('Study number: ')
                # Prevents loop if all input is valid
                need_to_loop = False
                # Append user input to file that user inputs (example: patients.txt)
                with open(patient_study_file_name,'a') as append:
                    append.write(patient_name + '\n' + patient_age + '\n' + patient_study + '\n\n')
                # Prompt user if user wants to ad another record + make the answer lower case with the .lower()
                add_additional_patient_record = input('Do you want to add another patient record (Y/N)? ').lower()
            except:
                print('Try again.')


def delete_patient_record():
    global patient_study_file_name
    import os
    loopee = 'y'
    while loopee == 'y':
        # Boolean variable as flag
        found = False

        # Ask which patient name to delete
        searchse = input('Patient name of the record to be deleted: ')
        searchse2 = input('Patient age of the record to be deleted: ')
        searchse3 = input('Patient study of the record to be deleted: ')

        # Open the original file
        deleteho = open(patient_study_file_name, 'r')

        # Open the temporary file
        deletehoho = open('test2.txt', 'w')

        # Read first study line of record's description field
        name_x = deleteho.readline()

        while (name_x != ''):
            age_x = deleteho.readline()
            study_x = deleteho.readline()
            blank = deleteho.readline()
            # Strip unecessary ends
            name_x = name_x.rstrip()
            age_x = age_x.rstrip()
            study_x = study_x.rstrip()

            if (name_x == searchse and age_x == searchse2 and study_x == searchse3):
                found = True

            else:
                # Print patient's name
                deletehoho.write(str(name_x) + '\n')
                deletehoho.write(str(age_x) + '\n')
                deletehoho.write(str(study_x) + '\n\n')

            # Break loop
            if age_x == '':
                break

            name_x = deleteho.readline()

        # Close the original and temporary file
        deleteho.close()
        deletehoho.close()

        # Remove and rename
        os.remove(patient_study_file_name)
        os.rename('test2.txt', patient_study_file_name)

        if found:
            print('Updated.')
        else:
            print('Patient record not found.')

        loopee = input('Do you want to delete another patient record (Y/N)? ').lower()

def count_patient_in_study():
    global patient_study_file_name
    # Boolean variable as flag
    found = False

    # Ask which patient name to delete
    searchse = input('Enter study number to see how many patient(s) is/are participating: ')

    # Open the original file
    deleteho = open(patient_study_file_name, 'r')

    # Read first record's description field
    count = 0
    for study in deleteho.read().split():
        if study != searchse:
            continue
        else:
            count += 1
            found = True
            continue

    if found:
        print('There are ',count,' patient(s) in Study ',searchse,'.')
    else:
        print('Study number not found.')

def display_patient_in_study():
    global patient_study_file_name
    # Boolean variable as flag
    found = False

    # Ask which patient name to delete
    searcho = input('Enter study number to display the names of patient(s) that is/are participating: ')

    # Open the original file
    deleteho = open(patient_study_file_name, 'r')

    # Read first study line of record's description field
    name_x = deleteho.readline()
    age_x = deleteho.readline()
    study_x = deleteho.readline()

    # Strip unecessary ends
    name_x = name_x.rstrip()
    age_x = age_x.rstrip()
    study_x = study_x.rstrip()

    print('Patient(s) Participating: ')
    while(study_x != ''):
        # Strip unecessary ends
        name_x = name_x.rstrip()
        age_x = age_x.rstrip()
        study_x = study_x.rstrip()

        if study_x == searcho:
            # Print patient's name
            print(name_x)
            found = True

        # Read continuing lines
        blank = deleteho.readline()
        name_x = deleteho.readline()
        age_x = deleteho.readline()
        study_x = deleteho.readline()

    # Close the file
    deleteho.close()

    if found:
        print()
    else:
        print('None')
        print('Study number not found.')


def display_patient_record():
    global patient_study_file_name
    # Open the original file
    deleteho = open(patient_study_file_name, 'r')
    # Read first line of record's description field
    namename = deleteho.readline()
    # Read the rest of the file
    print('Patient Study Report')
    while namename != '':
        # Read the other fields
        ageage = deleteho.readline()
        studystudy = deleteho.readline()
        blank = deleteho.readline()

        # Strip the \n from the description
        namename = namename.rstrip('\n')
        ageage = ageage.rstrip('\n')
        studystudy = studystudy.rstrip('\n')

        # Display the record
        print('Patient Name: ', namename)
        print('Patient Age: ', ageage)
        print('Patient Study: ', studystudy)
        print()

        # Read next description
        namename = deleteho.readline()

    # Close the file
    deleteho.close()

def tally_patients_by_study():
    from collections import Counter
    global patient_study_file_name
    deleteho = open(patient_study_file_name, 'r')
    # Create list
    list1 = []

    # TAG 1/3
    nameee = deleteho.readline()
    ageee = deleteho.readline()
    while nameee != '' and ageee != '':
        # TAG 2/3
        studyee = deleteho.readline()
        blankee = deleteho.readline()

        # Strip the \n from the description
        nameee = nameee.rstrip('\n')
        ageee = ageee.rstrip('\n')
        studyee = studyee.rstrip('\n')

        # Append current study to list
        list1.append(studyee)

        # TAG 3/3
        nameee = deleteho.readline()
        ageee = deleteho.readline()

    deleteho.close()

    # Print output
    print('Patients Per Study')
    print("Counter({'Study Number' : Total Patient(s)})")
    print(Counter(list1))

def search_patient():
    global patient_study_file_name
    repeat = 'y'
    while repeat == 'y':
        # Delete this later
        patient_study_file_name = 'test1.txt'
        # Delete this later

        # Input from user
        print('Search Patient Record by Patient Name')
        searchez = input('Patient Name= ')

        found = False
        deleteho = open(patient_study_file_name, 'r')
        # TAG 1/3
        namez = deleteho.readline()
        agez = deleteho.readline()

        while namez != '':
            # TAG 2/3
            studyz = deleteho.readline()
            blankz = deleteho.readline()
            # Strip the \n from the description
            namez = namez.rstrip('\n')
            agez = agez.rstrip('\n')
            studyz = studyz.rstrip('\n')

            if namez == searchez:
                # Display the record
                found = True
                print('Patient Name: ', namez)
                print('Patient Age: ', agez)
                print('Patient Study: ', studyz)
                print()
                break

            # TAG 3/3
            namez = deleteho.readline()
            agez = deleteho.readline()

        deleteho.close()
        if found:
            print('Process finished.')
        else:
            print('Patient name not found.')
        repeat = input('Do you want to search for another patient record (Y/N)? ').lower()

# Run file
menu()
# Mark the end of the program
print('\nEnd of program. \nBy Celine Yuwono.')

# Prompt to exit Python
input("Press Enter to exit.")