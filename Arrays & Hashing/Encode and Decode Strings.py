def encode(strs):
    return ":;".join(strs)


def decode(strs):
    return strs.split(":;")