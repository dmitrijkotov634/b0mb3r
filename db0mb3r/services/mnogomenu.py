from db0mb3r.services.service import Service


class MnogoMenu(Service):
    async def run(self):
        await self.get(
            f"http://mnogomenu.ru/office/password/reset/{self.format(self.formatted_phone, '+* (***) *** ** **')}",
        )
