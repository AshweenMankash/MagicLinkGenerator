from DatabaseOperations.Base import Base


class VerifyMailOperations(Base):
    def __init__(self):
        super().__init__("verifyMailService")

    def store_mail_data_for_verification(self, email, ip_addr, code):
        self._db.hset(
            email, mapping={"email": email, "ip_address": ip_addr, "code": code}
        )
        self._db.expire(email, 60 * 15)

    def verify_mail_data_for_verification(self, email, code):
        data = self._db.hget(email, key="code")
        if data is None:
            return {"msg": "Code Expired", "verification_status": False}
        data = data.decode()
        if data is not None and data == code:
            resp = self._db.delete(email)
            return {"msg": "Code Verified", "verification_status": True}
        return {"msg": "Incorrect Code", "verification_status": False}