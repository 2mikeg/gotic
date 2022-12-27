from typing import Dict, List, Optional

import gotic.models as models
from gotic.camel_to_snake import camel_to_snake
from gotic.create_file import class_to_go_struct
from gotic.reader import reader
from gotic.translate_type import PYDANTIC_TO_GO_TYPES


def process_mapped_items(
    mapped_item: Dict, json_flag: Optional[bool] = False
) -> models.MappingModelItem:

    i = mapped_item[1]

    item_title = i["title"].replace(" ", "")
    item_type = i["type"]

    mapped_item_object = models.MappingModelItem(
        key_to_go=item_title,
        type_to_go=PYDANTIC_TO_GO_TYPES[item_type],
        json_name=camel_to_snake(item_title) if json_flag else None,
    )

    return mapped_item_object


def map_models(
    in_models: List, json_flag: Optional[bool] = False
) -> models.MappingModelClass:

    for model in in_models:

        model_schema = model.schema()

        model_name = model_schema["title"]
        model_properties = model_schema["properties"]

        model_required_items = model_schema["required"]

        mapped_items = [
            process_mapped_items(item, json_flag) for item in model_properties.items()
        ]

        yield models.MappingModelClass(
            model_name=model_name,
            items_mapping=mapped_items,
            required_items=model_required_items,
        )


def map_files(models_folder: str) -> None:

    read_response = reader(models_folder)

    models_list = list(read_response)
    list_mapped_models = [
        (model.filename, map_models(model.classes)) for model in models_list
    ]

    for name, l in list_mapped_models:
        class_to_go_struct(filename=name, models_list=list(l))
