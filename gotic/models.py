from typing import List, Optional

from pydantic import BaseModel


class MappingModelItem(BaseModel):
    key_to_go: str
    type_to_go: str
    json_name: Optional[str] = None


class MappingModelClass(BaseModel):
    model_name: str
    items_mapping: List[MappingModelItem]
    required_items: List


class ReadFileResponse(BaseModel):
    filename: str
    classes: List
