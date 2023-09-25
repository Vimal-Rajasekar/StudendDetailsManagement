'''Importing Necessary Packages'''
import student_actions
import staff_actions
import mail_sending_actions
import Registration_Process
import staffs_details
import mysql.connector

# Connecting my database with this mydb variable.
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="aamec_db"
)
'''Creating a Variable for Cursor Function which Serves as a Pipeline Between Python and MySql Database.'''
mycursor=mydb.cursor()

def welcome_message():
    '''Printing Welcome Message at Center'''

    print("\n","Welcome to AAMEC Results Portal\n".center(150))

def main_function():
    '''Main Logic Of this Application is Defined Here.'''

    try:
        '''Getting Input From User Inside Try Block To Catch the Exception if any!'''
        member=int(input("Enter 1 For Staff OR 2 For Student:"))
        if member==1:
            '''Member = 1 means it's a Staff Who is Using Our Application'''
            def purpose_input():
                try:
                    '''Getting the Purpose(Register/Login) Of Visiting Our Application From Staff Inside Try Block To Catch the Exception if any!'''
                    purpose=int(input("Enter 1 For Register OR 2 For Login:"))
                    if  purpose==1:
                        '''purpose = 1 means Staff is Trying To Register In Our Application'''
                        def register_purpose():
                            try:
                                '''Getting User Info to Register Inside Try To Catch The Exception If Any!'''
                                mail_id = input("Enter Your Mail ID:") #Getting Mail Id to send OTP to Verify and Register
                                user_name = input("Enter Your UserName:") #Getting Staff Name to Use Throughout Our Application,to Mention Staff.

                                def input_password():
                                    '''Getting Password from Staff Inside a Function So that when he Enters the distinct Passwords we can call this Function to ask again'''

                                    try:
                                        '''Getting Password from User to Register Inside Try To Catch The Exception If Any!'''
                                        password=input("Enter Your Password:")#Getting Password
                                        reenter_password=input("Re-Enter Your Password:")#Asking again to Verify

                                        if password==reenter_password:#Checking Whether the both passwords are Matching.
                                            if user_name and password and mail_id:
                                                mail_sending_actions.send_mail(user_name,password,mail_id)#Calling the send_mail() to Sent OTP to Staff EmailId for Register
                                            else:
                                                print("Please Provide Required Details to Continue!")
                                                register_purpose()
                                        else:#If Both passwords are Distinct,Intimate Staff about it and Ask Password Again from Staff.
                                            print("Oops!InCorrect PassWord-Password Mismatch")
                                            def forgot_password1():
                                                try:
                                                    forgot_password=int(input("Enter 1 To Retry Password Or 2 To Exit:"))
                                                    if forgot_password==1:
                                                        input_password()#Calling input_password() to Ask the Password to the Staff Again.
                                                    elif forgot_password==2:
                                                        print("Thank You For Visiting Our Application!")
                                                    else:
                                                        print("Please Enter Correct Choice")
                                                        forgot_password1()
                                                except Exception as e:
                                                    print("Invalid Input Caused",e)
                                                    forgot_password1()

                                    except Exception as e:
                                        print("Invalid Input Caused",e)
                                        input_password()
                                input_password()  # Calling the input_password() to Get the Password From User.
                            except Exception as e:
                                print("Invalid Input Caused", e)
                                register_purpose()
                        register_purpose()

                    elif purpose==2:
                        '''purpose = 2 means Staff is Trying To Login In Our Application'''
                        def login_purpose():
                            try:
                                '''Getting User Name and Mail Id from Staff to Verify and allow them to Login'''

                                user_name=input("Enter Your User Name For Login:")#Getting User Name
                                mail_id=input("Enter Your Email Id For Login:")#Getting Mail ID
                                user_id=int(input("Please Enter Your User ID Which Is Provided With Your Registration:"))#Getting User Id, Provided After Registration
                                if user_name and mail_id and user_id:
                                    Registration_Process.login_staff(user_name,mail_id,user_id)#Calling Login_staff() Function to verify and Login the Staff

                                else:
                                    print("Please Provide Required Details to Continue!")
                                    login_purpose()
                            except Exception as e:
                                print("Invalid Input Caused",e)
                                login_purpose()
                        login_purpose()
                except Exception as e:
                    print("Invalid Input Caused",e)

                    def retry_input1():
                        try:
                            retry_input = int(input("Enter 1 to Register/Login or 2 to Exit:"))
                            if retry_input == 1:
                                purpose_input()
                            elif retry_input == 2:
                                print("Thank You For Visiting Our Application!")
                            else:
                                print("Invalid Input!Please Enter Correct Input:")
                                retry_input1()
                        except Exception as e:
                            print("Invalid Input Caused", e)
                            retry_input1()

                    retry_input1()
            purpose_input()

            '''                Student Activities                           '''

        elif member==2:
            '''Member = 2 means it's a Student Who is Using Our Application'''
            def getting_studentchoice():
                while True:#Using Infinite While Loop to Allowing the Student to View the Semester Results of Many Students Until he/she Exits.
                    try:
                        student_choice = int(input("Enter 1 to View Results or 2 to Exit:"))#Getting Student choice to confirm whether they want to See Results or Not

                        if student_choice==1:#If their choice is 1,then
                            student_actions.view_results()#Call the view_results Funtion to ask their Details and Displaying Their Result

                        elif student_choice==2:#If their choice is 2,then
                            print("Thank You For Visiting Our Application!")#Display Thanking Message and Exit
                            break

                        else:#When their choice is Other than 1 or 2,Ask Them Again
                            print("Please Enter Correct Choice!")
                            getting_studentchoice()

                    except Exception as e:
                        print("Invalid Input Caused", e)
                        getting_studentchoice()

            getting_studentchoice()#Calling getting_studentchoice() to Ask Student Choice Whether to display Result or Not.

        else:
            print("Please Enter Correct Choice!")
            main_function()

    except Exception as e:
        print("Invalid Input Caused",e)
        def retry_input1():
            try:
                retry_input = int(input("Enter 1 to Retry or 2 to Exit:"))
                if retry_input == 1:
                    main_function()
                elif retry_input == 2:
                    print("Thank You For Visiting Our Application!")
                else:
                    print("Invalid Input!Please Enter Correct Input:")
                    retry_input1()
            except Exception as e:
                print("Invalid Input Caused", e)
                retry_input1()

        retry_input1()


if __name__=="__main__":
    welcome_message()
    main_function()