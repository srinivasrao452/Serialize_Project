
import json

class SerializeMixin(object):
    def user_defined_serailze(self,qs):
        p_data = json.loads(qs)

        emp_list = []

        for obj in p_data:
            emp = obj['fields']
            emp_list.append(emp)

        json_data = json.dumps(emp_list)

        return json_data


def is_json(data):
    try:
        p_data = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid





