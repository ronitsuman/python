
# import smtplib

# smtp_server = 'smtp.example.com'
# port = 587  # For starttls

# try:
#     server = smtplib.SMTP(smtp_server, port)
#     server.ehlo()  # Can be omitted
#     server.starttls(context=ssl.create_default_context())  # Secure the connection
#     server.ehlo()  # Can be omitted
#     print("Connection to SMTP server successful")
#     server.quit()
# except Exception as e:
#     print(f"An error occurred: {e}")