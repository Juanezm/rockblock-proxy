import logging
from fastapi import FastAPI

from rockblock_proxy.config import LOG_LEVEL, LOG_FORMAT
from rockblock_proxy.model import RBMessage
from rockblock_proxy.repository import InfluxDBRepository

logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/")
async def receive(msg: RBMessage):
    logger.info(f"Received: '{msg}")
    repo = InfluxDBRepository()
    return repo.add(msg)
