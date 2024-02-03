import json

def get_spn(toponym):
    values = iter(toponym.get("boundedBy").get("Envelope").values())
    x1, y1 = map(float, next(values).split())
    x2, y2 = map(float, next(values).split())
    return f"{x2 - x1},{y2 - y1}"


def get_ll(toponym):
    coords = toponym["Point"]["pos"]
    longitude, lattitude = coords.split(" ")

    return ",".join([longitude, lattitude])
