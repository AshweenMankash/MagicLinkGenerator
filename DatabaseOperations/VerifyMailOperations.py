from DatabaseOperations.Base import Base


class VerifyMailOperations(Base):
    def __init__(self):
        super().__init__("verifyMailService")

    
    def store_mail_data_for_verification(self, email, ip_addr, code):
        self._db.hset(email,mapping={
            "email": email,
            "ip_address": ip_addr,
            "code": code
        })
    
    def verify_mail_data_for_verification(self,email, code):
        data = self._db.hget(email)
        if data is not None and data.get("code") == code:
            return True
        return False




