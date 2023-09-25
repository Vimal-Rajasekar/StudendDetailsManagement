import main_file
import student_actions
import mail_sending_actions
import staffs_details
def  add_details():
    '''                       Adding Student Details          '''
    sql="insert into students_results (Register_Number,First_Name,Last_Name," \
        "Email_Id,Semester,Subject_1,Subject_2,Subject_3,Subject_4,Subject_5,Subject_6,Total_Marks,Average,Result) " \
        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        reg_no=int(input("Enter Student Register Number:"))
        first_name = input("Enter Student First Name:")
        last_name = input("Enter Student Last Name:")
        email_id=input("Enter Student Email Id:")
        sem = int(input("Enter Semester Number:"))
        sub1 = int(input("Enter Subject 1 Marks:"))
        sub2 = int(input("Enter Subject 2 Marks:"))
        sub3 = int(input("Enter Subject 3 Marks:"))
        sub4 = int(input("Enter Subject 4 Marks:"))
        sub5 = int(input("Enter Subject 5 Marks:"))
        sub6 = int(input("Enter Subject 6 Marks:"))
        total_mark=sub1+sub2+sub3+sub4+sub5+sub6
        average=(sub1+sub2+sub3+sub4+sub5+sub6)/6
        result=''
        if sub1 >=45 and sub2 >=45 and sub3 >=45 and sub4 >=45 and sub5 >=45 and sub6 >=45:
            result="Pass"
        else:
            result="Fail"
        if reg_no and first_name and last_name and sem and sub1 and sub2 and sub3 and sub4 and sub5 and sub6:
            values=(reg_no,first_name,last_name,email_id,sem,sub1,sub2,sub3,sub4,sub5,sub6,total_mark,average,result)
            main_file.mycursor.execute(sql,values)
            main_file.mydb.commit()
            print("Data Added Successfully!")
        else:
            print("Please Enter Required Details To Add!")
    except Exception as e:
        print("Invalid Input Caused", e)
        def add_resultagain():
            try:
                add_again=int(input("Enter 1 If You Want to Add Again Or 2 to Exit:"))
                if add_again==1:
                    add_details()
                elif add_again==2:
                    print("Thank You!Please Continue to Your Process")
                else:
                    print("Invalid Input!Please Enter Correct Choice")
                    add_resultagain()
            except Exception as e:
                print("Invalid Input Caused", e)
                add_resultagain()
        add_resultagain()

def read_details():
    '''               Read Data from DataBase               '''
    sql="select * from students_results"
    main_file.mycursor.execute(sql)
    result = main_file.mycursor.fetchall()
    if result:
        print("\nStudent Details Management Application\n".center(230))
        for row in result:
            print('S.No:',row[0],'| Register Number:',row[1],'| First Name:',row[2],'| Last Name:',row[3],'| Semester:',row[5],'| Subject 1 Marks:',row[6],
                  '| Subject 2 Marks:',row[7],'| Subject 3 Marks:',row[8],'| Subject 4 Marks:',row[9],'| Subject 5 Marks:',row[10],
                  '| Subject 6 Marks:',row[11],'| Total Marks:',row[12],'| Average:',row[13],'| Result:',row[14])
    main_file.mydb.commit()
    print("Data Fetched Successfully!")
def update_details():
    '''           Updating Student Data             '''
    try:
        s_no=int(input("Enter Serial Number to Update Student Data:"))
        column_name=input("Enter Which Data You Want To Update From Below Available Datas:\n Register_Number | First_Name |  Last_Name | Semester"
                          "| Subject_1 Marks| Subject_2 Marks| Subject_3 Marks| Subject_4 Marks| Subject_5 Marks| Subject_6 Marks"
                          "| Total_Marks| Average| Result")
        if column_name=="First_Name" or column_name=="Last_Name" or column_name=="Email_Id" or column_name=="Register_Number" or column_name=="Result":
            try:
                name=input(f"Enter the Value for {column_name} to Update Existing Data:")
                if name:
                    sql=f"UPDATE students_results SET {column_name} = %s WHERE `S.No` = %s"
                    main_file.mycursor.execute(sql,(name,s_no,))
                    main_file.mydb.commit()
                    print("Data Updated Successfully!")
                else:
                    print("Please Enter Valid Data!")
                    update_details()
            except Exception as e:
                print("Invalid Input Caused", e)

                def retry_input1():
                    try:
                        retry_input = int(input("Enter 1 to Retry Update or 2 to Exit:"))
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

        elif column_name not in["Semester","Subject_1","Subject_2","Subject_3","Subject_4","Subject_5","Subject_6","Total_Marks",
                                "Average"]:
            print("Oops!,Invalid Data.Can't Update the Data which doesn't Exist")
            update_details()
        else:
            def update_data():
                try:
                    value = int(input(f"Enter the Value for {column_name} to Update Existing Data:"))
                    sql = f"UPDATE students_results SET {column_name} = %s WHERE `S.No` = %s"
                    main_file.mycursor.execute(sql,(value,s_no,))
                    main_file.mydb.commit()
                    print("Data Updated Successfully!")
                except Exception as e:
                    print("Invalid Input Caused", e)

                    def retry_input1():
                        try:
                            retry_input = int(input("Enter 1 to Retry Update or 2 to Exit:"))
                            if retry_input == 1:
                                update_data()
                            elif retry_input == 2:
                                print("Thank You For Visiting Our Application!")
                            else:
                                print("Invalid Input!Please Enter Correct Input:")
                                retry_input1()
                        except Exception as e:
                            print("Invalid Input Caused", e)
                            retry_input1()

                    retry_input1()
            update_data()
    except Exception as e:
        print("Invalid Input Caused", e)

        def retry_input1():
            try:
                retry_input = int(input("Enter 1 to Retry Update or 2 to Exit:"))
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

def delete_details():
    '''                        Deleting Data from DataBase                       '''
    try:
        column_name = input("Enter Which Data You Want To Delete From Below Available Datas:\n Register_Number | First_Name |  Last_Name | Semester"
                          "| Subject_1 Marks| Subject_2 Marks| Subject_3 Marks| Subject_4 Marks| Subject_5 Marks| Subject_6 Marks"
                          "| Total_Marks| Average| Result")
        if column_name == "First_Name" or column_name == "Last_Name" or column_name=="Email_Id" or column_name=="Register_Number":
            try:
                name = input(f"Enter the Value Of Student Data for {column_name} to Delete from Database:")
                sql = f"DELETE FROM students_results WHERE {column_name} = %s"
                main_file.mycursor.execute(sql, (name,))
                main_file.mydb.commit()
                print("Data Deleted Successfully!")
            except Exception as e:
                print("Invalid Input Caused", e)

                def retry_input1():
                    try:
                        retry_input = int(input("Enter 1 to Retry Delete or 2 to Exit:"))
                        if retry_input == 1:
                            delete_details()
                        elif retry_input == 2:
                            print("Thank You For Visiting Our Application!")
                        else:
                            print("Invalid Input!Please Enter Correct Input:")
                            retry_input1()
                    except Exception as e:
                        print("Invalid Input Caused", e)
                        retry_input1()

                retry_input1()


        elif column_name not in ["Semester", "Subject_1", "Subject_2", "Subject_3","Subject_4", "Subject_5", "Subject_6",
                                 "Total_Marks", "Average", "Result", "S.No"]:
            print("Oops! Invalid Data. Can't Delete Data That Doesn't Exist")
            delete_details()
        # elif column_name == 'S.No':
        #     try:
        #         value = int(input("Enter the Value Of Student Data to Delete from DataBase:"))
        #         sql = f"DELETE FROM students_results WHERE `S.No` = %s"
        #         main_file.mycursor.execute(sql, (value,))
        #         main_file.mydb.commit()
        #         print("Data Deleted Successfully!")
        else:
            def delete_data1():
                try:
                    value = int(input(f"Enter the Student Data for {column_name} to Delete from DataBase:"))
                    sql = f"DELETE FROM students_results WHERE `{column_name}` = %s"
                    main_file.mycursor.execute(sql, (value,))
                    main_file.mydb.commit()
                    print("Data Deleted Successfully!")
                except Exception as e:
                    print("Invalid Input Caused", e)
                    def retry_input1():
                        try:
                            retry_input = int(input("Enter 1 to Retry Delete or 2 to Exit:"))
                            if retry_input == 1:
                                delete_data1()
                            elif retry_input == 2:
                                print("Thank You For Visiting Our Application!")
                            else:
                                print("Invalid Input!Please Enter Correct Input:")
                                retry_input1()
                        except Exception as e:
                            print("Invalid Input Caused", e)
                            retry_input1()

                    retry_input1()
            delete_data1()

    except Exception as e:
        print("Invalid Input Caused", e)

        def retry_input1():
            try:
                retry_input = int(input("Enter 1 to Retry Delete or 2 to Exit:"))
                if retry_input == 1:
                    delete_details()
                elif retry_input == 2:
                    print("Thank You For Visiting Our Application!")
                else:
                    print("Invalid Input!Please Enter Correct Input:")
                    retry_input1()
            except Exception as e:
                print("Invalid Input Caused", e)
                retry_input1()

        retry_input1()

def staff_activities():
    '''Function Containing Activities that can be performed by Staffs After Login'''
    while True:
        print("Enter 1 for Add Student Details")
        print("Enter 2 for View Student Details")
        print("Enter 3 for Update Student Details")
        print("Enter 4 for Delete Student Details")
        print("Enter 5 for Sending Notifications")
        print("Enter 6 for Update Your Own Details")
        print("Enter 7 for Changing Your Password")
        print("Enter 8 to Exit")
        try:
            your_choice=int(input("Enter Your Choice:"))
            if your_choice==1:
                add_details()
            elif your_choice==2:
                read_details()
            elif your_choice==3:
                update_details()
            elif your_choice==4:
                delete_details()
            elif your_choice==5:
                mail_sending_actions.send_notifications()
            elif your_choice==6:
                staffs_details.update_details()
            elif your_choice==7:
                staffs_details.change_password()
            elif your_choice==8:
                print("Thank You For Visiting Our Application!")
                break
            else:
                print("Please Enter Correct Choice!")
        except Exception as e:
            print("Invalid Input Caused",e)


if __name__=="__main__":
    main_file.welcome_message()
    main_file.main_function()