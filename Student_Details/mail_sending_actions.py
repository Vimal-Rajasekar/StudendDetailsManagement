'''Mail Sending To Both Students and Staff'''
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Registration_Process
import main_file

"""Generate a random OTP of the specified length(6)."""
otp_length=6
otp = ''.join([str(random.randint(0, 9)) for _ in range(otp_length)])
# random.randint(000000,999999)
# Email configuration
def send_mail(user_name,password,reciever_mail):
    sender_email = "vimsdvimal0@gmail.com"
    receiver_email = reciever_mail
    subject = "One Time Password For Login"
    message_body = f"""Welcome To Student Details Management Application\n
Confirmation OTP for Student Details Management System Application\nOTP:{otp}"""

    # SMTP server configuration (for Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Port for TLS

    # Your email account credentials
    username = "vimsdvimal0@gmail.com"
    password = "wcchlfpmyjrdvjxs"

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(message_body, "plain"))

    # Connect to the SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Enable TLS encryption
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("OTP Sent To Your Email Successfully!")
        def otp_verification():
            try:
                otp_num=input("Enter OTP Sent To Your Email:")
                if otp == otp_num:
                    Registration_Process.register_staffs(user_name,password,reciever_mail)

                else:
                    print("Oops! Wrong OTP!")
                    def retry_otp():
                        try:
                            retry_otp=int(input("Enter 1 to Retry Otp or 2 to Resend Otp or 3 to Exit:"))
                            if retry_otp==1:
                                otp_verification()
                            elif retry_otp==2:
                                send_mail(user_name,password,reciever_mail)
                            elif retry_otp==3:
                                print("Thank You For Visiting Our Application!")
                            else:
                                print("Invalid Input!Please Enter Correct Input:")
                                retry_otp()
                        except Exception as e:
                            print("Invalid Input Caused", e)
                    retry_otp()

            except Exception as e:
                print("Invalid Input Caused",e)
        otp_verification()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        server.quit()  # Close the SMTP server connection

def send_notifications():
    sql="select Email_Id from students_results"
    main_file.mycursor.execute(sql)
    email_id=main_file.mycursor.fetchall()
    sender_email = "vimsdvimal0@gmail.com"
    subject = "Results Published!"
    message_body = f"""Hello! Dearest Students of AAMEC\n
Your Semester Results Has Been Published.Please Check It Out On Our Application.\n
Thank You."""

    # SMTP server configuration (for Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Port for TLS

    # Your email account credentials
    username = "vimsdvimal0@gmail.com"
    password = "wcchlfpmyjrdvjxs"

    # Create the email message
    for outer_data in email_id:
        for student_email in outer_data:
            if student_email!="undefined" or student_email!=None or student_email!="null":
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = student_email
                message["Subject"] = subject
                message.attach(MIMEText(message_body, "plain"))

                # Connect to the SMTP server
                try:
                    server = smtplib.SMTP(smtp_server, smtp_port)
                    server.starttls()  # Enable TLS encryption
                    server.login(username, password)
                    server.sendmail(sender_email, student_email, message.as_string())
                    print("Notifications Sent SuccessFully!")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
    
                finally:
                    server.quit()  # Close the SMTP server connection

    main_file.mydb.commit()

if __name__=="__main__":
    main_file.welcome_message()
    main_file.main_function()

