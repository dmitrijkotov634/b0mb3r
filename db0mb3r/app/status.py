from asyncio import Task
from typing import Dict, Union, Optional

status: Dict[str, Dict[str, Optional[Union[str, int]]]] = {}

attack_tasks: Dict[str, Task] = {}
