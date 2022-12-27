import time
from typing import List

from mako.template import Template  # type: ignore

import gotic.models as models


def class_to_go_struct(
    filename: str, models_list: List[models.MappingModelClass]
) -> None:

    template = Template(filename="gotic/templates/base.txt")

    template_rendered = template.render(models_list=models_list)

    file = open(f"{int(time.time())}_{filename}.go", "wt")
    file.write(template_rendered)

    file.close()
