from tortoise import models, fields
from passlib.hash import bcrypt


class UserAuth(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password_hash = fields.CharField(max_length=255)

    def verify_password(self, password):
        verification = bcrypt.verify(password, self.password_hash)
        return verification
