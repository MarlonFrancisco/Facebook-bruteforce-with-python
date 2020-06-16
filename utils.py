import re
from functools import reduce


def get_element(document, el):
    reg = re.compile(f"(<{el}.*>.*</{el}>)|(<{el}.*/>)", re.I)
    return reg.split(document)[1]


def convert_form_to_dict(form):
    reg = re.compile(r"(<)", re.I)
    list_elements = reg.split(form)

    callback_filter = lambda x: -1 not in [x.find("input"), x.find("name="), x.find("value=")]

    inputs = filter(callback_filter, list_elements)
    def callback_reducer(acc, crr):
        reg = re.compile(r"name=\"(.*?)\".*value=\"(.*?)\"", re.I)
        p = reg.search(crr).groups()
        acc[p[0]] = p[1]
        return acc

    data = reduce(callback_reducer, inputs, {})
    return data
