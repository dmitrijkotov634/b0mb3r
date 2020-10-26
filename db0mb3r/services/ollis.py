from db0mb3r.services.service import Service


class Ollis(Service):
    async def run(self):
        await self.post(
            "https://www.ollis.ru/gql",
            json={
                "query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'
                % self.formatted_phone
            },
        )
