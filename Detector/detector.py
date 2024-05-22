import mysql.connector
import smtplib
from email.mime.text import MIMEText

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loginInfo"
)

# Read the file and search for the specific text
with open("file.txt", "r") as f:
    content = f.read()
    if "specific_text" in content:
        # Search for the text in the MySQL database
        cursor = db.cursor()
        query = "SELECT gmail, server_name, text_to_receive FROM admin_config WHERE text_to_receive = %s"
        cursor.execute(query, ("specific_text",))
        result = cursor.fetchone()
        if result:
            # Set the subject and text of the email
            subject = result[1]
            text = result[2] + " " + "specific_text"
            # Send an email alert using the Postfix server on a different machine
            msg = MIMEText(text)
            msg["Subject"] = subject
            msg["From"] = "sender@example.com"
            msg["To"] = result[0]
            server = smtplib.SMTP(result[1], 25)
            server.login("username", "password")
            server.sendmail("sender@example.com", result[0], msg.as_string())
            server.quit()
            print("Email alert sent to", result[0])
        else:
            print("No matching text found in the database")
    else:
        print("Specific text not found in the file")