I need to apply for a civil service position. I want to do it with organisations in the startup/entrpreneurship ecosystem. How do I do it without having to manually add subject each time or the attachchment.

### **Voila**

# ManyMail: Email Automation Script

This project is a Python script designed to automate the process of sending personalized emails with attachments to multiple recipients. It is particularly useful for job applications, networking, or any scenario where you need to send similar emails to different contacts.

## Features

- Sends personalized emails to a list of recipients.
- Supports HTML formatting for rich text emails.
- Attaches multiple files to each email.
- Uses environment variables for secure handling of email credentials.

## Setup

### Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/installation/)
- [yagmail](https://github.com/kootenpv/yagmail) for sending emails
- [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/email-automation.git
   cd email-automation
   ```

2. **Install the required packages**:

   ```bash
   pip install yagmail python-dotenv
   ```

3. **Set up environment variables**:

   Create a `.env` file in the root directory and add your email credentials:

   ```plaintext
   sender_email=your_email@example.com
   sender_password=your_password
   ```

   **Note**: Use an app-specific password if your email provider requires it.

## Usage

1. **Edit the recipient list**:

   Open `send_emails.py` and update the `recipients` list with the names and email addresses of your contacts.

2. **Run the script**:

   Execute the script to send emails:

   ```bash
   python send_emails.py
   ```

3. **Verify emails**:

   Check the console output to ensure emails are sent successfully.

## Customization

- **Email Content**: Modify the `body` variable in `send_emails.py` to change the email content.
- **Attachments**: Update the `attachments` list to include any files you want to send.
