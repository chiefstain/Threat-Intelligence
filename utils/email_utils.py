import smtplib
import json

def send_email_alert(results):
    sender_email = "your_email@example.com"
    receiver_email = "recipient@example.com"
    password = "your_email_password"

    subject = "Shodan Alert: Results Found"
    body = f"Results:\n{json.dumps(results, indent=4)}"

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("Alert email sent!")
    except Exception as e:
        print(f"Error sending email: {e}")
