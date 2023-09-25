import main_file
import staff_actions

def register_staffs(user_name,password,staff_Email):
    '''Adding Staffs Details into the Staffs Table'''
    sql="Insert into aamec_staffs(User_Name,Staff_password_forLogin,Email_Id) values(%s,%s,%s)"
    value=(user_name,password,staff_Email)
    main_file.mycursor.execute(sql,value)
    main_file.mydb.commit()
    print(f"Dear {user_name}.Your Details Have Been Successfully Registered!")
    sql1=f"select `Id_No`,Staff_password_forLogin,Email_Id from aamec_staffs where `User_Name`=%s"
    main_file.mycursor.execute(sql1,(user_name,))
    user_details=main_file.mycursor.fetchall()
    user_id=int(user_details[0][0])
    user_password=str(user_details[0][1])
    mail_id=str(user_details[0][2])
    print(f"Hey {user_name}!Your User Id  is {user_id}.Keep this User Id for  Login!.\nThank You!")
    main_file.mydb.commit()
    def ask_forlogin():
        try:
            login=int(input("Enter 1 to Login or 2 to exit:"))
            if login==1:
                user_name=input("Enter Your User Name:")
                mail_id = input("Enter Your Email Id:")
                user_id = input("Enter Your Id:")
                if user_name and mail_id and user_id:
                    login_staff(user_name,mail_id,user_id)
                else:
                    print("Please Provide Required Details To Continue")
                    ask_forlogin()
            elif login==2:
                print("Thank You For Visiting Our Application!")
            else:
                print("Please Enter Correct Choice!")
                ask_forlogin()
        except Exception as e:
            print("Invalid Input Caused",e)
            ask_forlogin()
    ask_forlogin()
def login_staff(user_name,mail_id,user_id):
    '''After Registered Using Email,Now Allowing Staffs to Login'''
    sql=f"select User_Name,Email_ID from aamec_staffs where `Id_No`=%s"
    main_file.mycursor.execute(sql,(user_id,))
    login_Data=main_file.mycursor.fetchall()
    main_file.mydb.commit()
    if  not login_Data:
        print("No Data Found!")
    else:
        for i in login_Data:
            if user_name==i[0] and mail_id==i[1]:
                print(f"Hey {user_name}.You Have Been Logged In Successfully!")
                staff_actions.staff_activities()
            else:
                print("Oops!Invalid User Name or Email Id")
                raise Exception




if __name__=="__main__":
    main_file.welcome_message()
    main_file.main_function()
