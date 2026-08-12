import locale


def slugify(value):
    return str(value).strip().lower().replace(" ", "-").replace("_", "-")


def money(value, currency="$"):
    locale.getdefaultlocale()
    return "%s%.2f" % (currency, float(value))


def titleize(value):
    return " ".join([part.capitalize() for part in str(value).split(" ")])
