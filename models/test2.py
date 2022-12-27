from pydantic import BaseModel

class ModelOne(BaseModel):
    dos: str
    tres: float

class ModelOneP(BaseModel):
    dos: str
    tres: float

class ModelOneZ(BaseModel):
    dos: str
    tres: float