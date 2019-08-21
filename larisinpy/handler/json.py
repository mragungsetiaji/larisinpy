
class JsonUtils(object):

    def __init__(self):
        pass

    def check_property(self, json_file, property):

        if isinstance(property, list):
            try:
                value = json_file[property[0]][property[1]]
            except:
                value = "ERROR404"
        else:
            try:
                value = json_file[property]
            except:
                value = "ERROR404"

        return value