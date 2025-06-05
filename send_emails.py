import yagmail
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define your email credentials
sender_email = os.getenv("sender_email")
sender_password = os.getenv("sender_password")

# Define the subject and attachments
subject = "Subject"
attachments = ["cv_filename.pdf", "cl_filename.pdf"]

# List of recipients
recipients = [
    {"name": "Firstname Lastname", "email": "random@yahoo.com"},
    {"name": "Firstname2 Lastname2", "email": "random2@yahoo.com"},
    {"name": "Firstname3 Lastname3", "email": "random3@yahoo.com"},
    # Add more recipients as needed
]

# Initialize the yagmail SMTP client with Yahoo's SMTP server
yag = yagmail.SMTP(
    user=sender_email, 
    password=sender_password,
    host='smtp.mail.yahoo.com', #find your correct host
    port=587, #find your correct port
    smtp_ssl=False,
    smtp_starttls=True
)

# Send emails
for recipient in recipients:
    body = (
        "I speak fluent finnish btw.<br><br>"
        f"Hi {recipient['name'].split()[0]},<br><br>"        
        "I am a 27-year-old experienced software developer with a host of other useful skills, "
        "and I would love to do my <b>2-month</b> civil service for your institution. This is because "
        "I am deeply interested in entrepreneurship, innovation, and Finland's startup ecosystem. "
        "I have attached a cover letter and CV - <b>let me solve some problems for you.</b><br><br>"
        "Best regards,<br>"
        "Firstname Lastname<br>"
        "random@yahoo.com | +358 0123456789<br>"
        "Helsinki<br><br>"
        '<a href="https://dev.to/pokumars">Dev blog/articles</a> | '
        '<a href="https://www.linkedin.com/in/oheneba-pm/">LinkedIn</a> | '
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