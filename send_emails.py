import yagmail
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define your email credentials
sender_email = os.getenv("sender_email")
sender_password = os.getenv("sender_password")

# Define the subject and attachments
subject = "Experienced Professional for Civil Service - test-user Surname"
attachments = ["cv_test-user_Surname_sivari.pdf", "cl_test-.pdf"]

# List of recipients
recipients = [
    {"name": "Outlook test-user", "email": "test-userkob@hotmail.com"},
    {"name": "Gmail test-user", "email": "test-userkob@gmail.com"},
    # Add more recipients as needed
]

# Initialize the yagmail SMTP client with Yahoo's SMTP server
yag = yagmail.SMTP(
    user=sender_email, 
    password=sender_password,
    host='smtp.mail.yahoo.com',
    port=587,
    smtp_ssl=False,
    smtp_starttls=True
)

# Send emails
for recipient in recipients:
    body = (
        f"Hi {recipient['name']},<br><br>"
        "I am a 27-year-old experienced software developer with a host of other useful skills, "
        "and I would love to do my <b>2-month</b> civil service for Aalto startup centre. This is because "
        "I am deeply interested in entrepreneurship, innovation, and Finland's startup ecosystem. "
        "I have attached a cover letter and CV - <b>let me solve some problems for you.</b><br><br>"
        "Best regards,<br><br>"
        "test-user Surname<br><br>"
        "test-userkob@yahoo.com | +358 44 282 6020<br><br>"
        "Helsinki<br><br>"
        '<a href="https://dev.to/pokumars">Dev blog/articles</a> | '
        '<a href="https://www.linkedin.com/in/test-user-pm/">LinkedIn</a> | '
        '<a href="https://github.com/pokumars">GitHub</a>'
    )
    yag.send(
        to=recipient['email'],
        subject=subject,
        contents=[body],
        attachments=attachments
    )
    print(f"Email sent to {recipient['name']} at {recipient['email']}")

print("All emails sent successfully!") 