import os
import smtplib
import logging

log = logging.Logger(__name__)

class Base:
    def __init__(self, secret) -> None:
        auth_key = os.getenv("SECRET")

        if secret != auth_key:
            raise ValueError("Invalid Secret")
        
        smtp_server = os.getenv("SMTP_SERVER")
        port = int(os.getenv("SMTP_PORT"))
        self.email = os.getenv("MAIL_ADDRESS")
        password = os.getenv("MAIL_PASSWORD")
        auth_key = os.getenv("SECRET")

        self.s = smtplib.SMTP_SSL(host=smtp_server, port=port)

        self.s.login(user=self.email, password=password)

    def send_mail(self, email, msg):
        err = self.s.sendmail(from_addr=self.email, to_addrs=email, msg=msg)
        log.error(err)
