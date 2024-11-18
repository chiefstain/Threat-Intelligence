def pretty_print(data):
    import json
    return json.dumps(data, indent=4, sort_keys=True)
