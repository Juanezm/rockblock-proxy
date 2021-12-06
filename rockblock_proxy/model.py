from pydantic import BaseModel


class RBMessage(BaseModel):
    imei: str
    serial: int
    momsn: int
    transmit_time: str
    iridium_latitude: float
    iridium_longitude: float
    iridium_cep: int
    data: bytes
