from tortoise.models import Model
from tortoise import fields


class City(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(30)
    country = fields.CharField(30)
