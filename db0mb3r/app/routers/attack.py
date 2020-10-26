import asyncio
import re
import uuid

import phonenumbers
from fastapi import APIRouter, HTTPException
from loguru import logger

from db0mb3r.app.models import AttackModel, StatusModel
from db0mb3r.app.status import status, attack_tasks
from db0mb3r.main import AttackLogic

router = APIRouter()


@logger.catch
@router.post("/start")
async def start_attack(attack: AttackModel):
    only_digits_phone = re.sub("[^0-9]", "", attack.phone)
    country_code = phonenumbers.parse(f"+{only_digits_phone}").country_code
    # May seem confusing, but phone is actually a full international phone: 79001234567

    attack_id = uuid.uuid4().hex
    status[attack_id] = {"started_at": None, "currently_at": None, "end_at": None}

    attack_logic = AttackLogic(
        attack_id, attack.number_of_cycles, country_code, only_digits_phone
    )

    task = asyncio.create_task(attack_logic.perform_attack())
    attack_tasks[attack_id] = task

    return {"success": True, "id": attack_id}


@logger.catch
@router.get("/{attack_id}/status", response_model=StatusModel)
def get_attack_status(attack_id: str):
    if attack_id not in status:
        raise HTTPException(status_code=404)
    return StatusModel(**status[attack_id])


@logger.catch
@router.post("/{attack_id}/stop")
def stop_attack(attack_id: str):
    if attack_id not in attack_tasks:
        raise HTTPException(status_code=404)

    status[attack_id]["currently_at"] = status[attack_id]["end_at"] = 1
    attack_tasks[attack_id].cancel()

    return {"success": True}
