from db0mb3r.services.service import Service


class Tele2TV(Service):
    async def run(self):
        await self.post(
            "http://tele2mwapp.cdnvideo.ru/api/v1/user/request-password.json",
            json={"MSISDN", self.formatted_phone}
        )
