import main_file
import random
import string
def view_results():
    '''                         Read Details from DataBase                       '''
    try:
        reg_no=input("Enter Your Register Number:")
        captcha_characters=string.ascii_letters+string.digits
        captcha_length=6
        captcha=''.join(random.choice(captcha_characters) for _ in range(captcha_length))
        print("Captcha:",captcha)
        def captch_verify():
            try:
                student_input=input("Enter The Captcha To Continue:")
                if student_input==captcha:
                    sql="select * from students_results where Register_Number=%s"
                    main_file.mycursor.execute(sql,(reg_no,))
                    results=main_file.mycursor.fetchall()
                    keys=['S.No','Register Number','First Name','Last Name','Email Id','Semester','Subject 1 Marks','Subject 2 Marks',
                          'Subject 3 Marks','Subject 4 Marks','Subject 5 Marks','Subject 6 Marks','Total Marks','Average','Result']
                    if results:
                        obtained_values=dict(zip(keys, results[0]))
                        print("Your Results:\n".center(120))
                        for datatype,valueofData in obtained_values.items():
                            if datatype=="S.No":
                                continue
                            print(datatype,valueofData,sep=':')
                    else:
                        print("No Results Found")
                else:
                    print("Oops! Wrong Captcha!")
            except Exception as e:
                print("Invalid Input Caused",e)

                def retry_input():
                    try:
                        retry_input = int(input("Enter 1 to Retry Captcha or 2 to Exit:"))
                        if retry_input == 1:
                            captch_verify()
                        elif retry_input == 2:
                            print("Thank You For Visiting Our Application!")
                        else:
                            print("Invalid Input!Please Enter Correct Input:")
                            retry_input()
                    except Exception as e:
                        print("Invalid Input Caused", e)
                        retry_input()

                retry_input()
        captch_verify()
    except Exception as e:
        print("Invalid Input Caused", e)
        def retry_input():
            try:
                retry_input = int(input("Enter 1 to Retry View Results or 2 to Exit:"))
                if retry_input == 1:
                    view_results()
                elif retry_input == 2:
                    print("Thank You For Visiting Our Application!")
                else:
                    print("Invalid Input!Please Enter Correct Input:")
                    retry_input()
            except Exception as e:
                print("Invalid Input Caused", e)
                retry_input()

        retry_input()

if __name__=="__main__":
    main_file.welcome_message()
    main_file.main_function()

