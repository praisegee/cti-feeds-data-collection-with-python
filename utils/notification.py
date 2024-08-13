import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from decouple import Csv, config


class Email(object):
    username = config("EMAIL_USER")
    password = config("EMAIL_PASSWORD")
    receiver_emails = config("EMAIL_RECEIVERS", cast=Csv())

    def __init__(self):
        self.server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.server.login(self.username, self.password)
        self.message = MIMEMultipart()

    def send(self, reports):
        self.message["From"] = f"PraiseGod <{self.username}>"
        self.message["Subject"] = "CTI APIs Notification"
        self.message.attach(MIMEText(reports, "plain"))
        self.server.sendmail(
            from_addr=self.username,
            to_addrs=self.receiver_emails,
            msg=self.message.as_string(),
        )
