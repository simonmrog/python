from tortoise.models import Model
from tortoise import fields
from app.services.aiohttp import http_client


class City(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(30)
    country = fields.CharField(30)
    timezone = fields.CharField(30)

    def current_time(self) -> str:
        return ""

    @classmethod
    async def get_current_time(cls, obj):
        response = await http_client.get(
            url=f"http://worldtimeapi.org/api/timezone/{obj.timezone}"
        )
        if "datetime" in response:
            current_time = response["datetime"]
            obj.current_time = current_time

    class PydanticMeta:
        computed = ("current_time", )
