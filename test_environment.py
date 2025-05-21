import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define your email credentials
sender_email = os.getenv("sender_email")
sender_password = os.getenv("sender_password")

print("Your Python environment is set up correctly!") 

print(f"Sender Email: {sender_email}")
print(f"Sender Password: {sender_password}")

