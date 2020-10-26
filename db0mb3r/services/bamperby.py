from db0mb3r.services.service import Service


class BamperBy(Service):
    async def run(self):
        await self.post(
            "https://bamper.by/registration/?step=1",
            data={
                "phone": "+" + self.formatted_phone,
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
        )
