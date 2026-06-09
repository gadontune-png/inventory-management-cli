def find_by_id(data, key, value):
    for item in data:
        if item.get(key) == value:
            return item
    return None