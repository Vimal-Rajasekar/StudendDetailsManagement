import main_file
def update_details():
    try:
        user_id = int(input("Enter Your User Id:"))
        column_name=input("Enter Which Data to Update:")
        value=input("Enter the New Value to Change:")
        sql=f"update aamec_staffs set {column_name}=%s where `Id_No`=%s"
        if user_id and column_name and value:
            main_file.mycursor.execute(sql,(value,user_id))
            main_file.mydb.commit()
            print("Data Updated SuccessFully!")
        else:
            print("Please Provide Required Details To Continue!")
    except Exception as e:
        print("Invalid Input Caused", e)
        def retry_input1():
            try:
                retry_input = int(input("Enter 1 to Retry Change Details or 2 to Exit:"))
                if retry_input == 1:
                    update_details()
                elif retry_input == 2:
                    print("Thank You For Visiting Our Application!")
                else:
                    print("Invalid Input!Please Enter Correct Input:")
                    retry_input1()
            except Exception as e:
                print("Invalid Input Caused", e)
                retry_input1()

        retry_input1()

def change_password():
    try:
        user_id=int(input("Enter Your User Id:"))
        password=input("Enter the New Password:")
        re_enter_password=input("Re-Enter the New Password:")
        if password==re_enter_password:
            if user_id and password:
                sql=f"update aamec_staffs set Staff_password_forLogin=%s where `Id_No`=%s"
                main_file.mycursor.execute(sql,(password,user_id))
                main_file.mydb.commit()
                print("Password Changed SuccessFully!")
            else:
                print("Please Provide Required Details To Continue!")
                change_password()
        else:
            print("InCorrect Password-Password Mismatch")
            def input_choice_for_change_password():
                try:
                    change_password1 = int(input("Enter 1 To Reset Password or 2 To Exit:"))
                    if change_password1==1:
                        change_password()
                    elif change_password1==2:
                        print("Thank You For Visiting Our Application!")
                    else:
                        print("Please Enter Valid Choice!")
                        input_choice_for_change_password()
                except Exception as e:
                    print("Invalid Input Caused",e)
                    input_choice_for_change_password()
            input_choice_for_change_password()
    except Exception as e:
        print("Invalid Input Caused", e)
        def retry_input1():
            try:
                retry_input = int(input("Enter 1 to Retry Change Password or 2 to Exit:"))
                if retry_input == 1:
                    change_password()
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
    main_file.welcome_message()
    main_file.main_function()