ROUTE_ZONES = {
    "SEA": "northwest",
    "PDX": "northwest",
    "SFO": "west",
    "LAX": "west",
    "DEN": "mountain",
}


def route_zone(code):
    return ROUTE_ZONES.get(code, "unknown")


def estimate_transit_days(origin, destination):
    if route_zone(origin) == route_zone(destination):
        return 1
    if "unknown" in (route_zone(origin), route_zone(destination)):
        return 5
    return 3


def build_route_label(origin, destination):
    return "{} to {}".format(origin, destination)
