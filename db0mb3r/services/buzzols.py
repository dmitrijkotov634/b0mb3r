from db0mb3r.services.service import Service


class Buzzols(Service):
    async def run(self):
        await self.get(
            "https://it.buzzolls.ru:9995/api/v2/auth/register",
            params={"phoneNumber": "+" + self.formatted_phone},
            headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"},
        )
