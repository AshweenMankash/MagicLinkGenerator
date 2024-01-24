import os
import smtplib


class Base:
    def __init__(self, secret) -> None:
        auth_key = os.getenv("mail_secret")

        if secret != auth_key:
            raise ValueError("Invalid Secret")

        smtp_server = os.getenv("smtp_server")
        port = int(os.getenv("smtp_port"))
        self.email = os.getenv("email_service_email")
        password = os.getenv("email_service_password")
        auth_key = os.getenv("mail_secret")

        self.s = smtplib.SMTP(host=smtp_server, port=port)

        self.s.login(user=self.email, password=password)

    def send_mail(self, email, msg):
        err = self.s.sendmail(from_addr=self.email, to_addrs=email, msg=msg)
        print(err)
