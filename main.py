from gotic.reader import reader

import gotic.mapping as mapping

from gotic.create_file import class_to_go_struct

c = reader("models")
c_list = list(c)
list_mapped_models = [(model.filename, mapping.map_model(model.classes)) for model in c_list]

for name, l in list_mapped_models:

    class_to_go_struct(filename=name, models_list=list(l))
