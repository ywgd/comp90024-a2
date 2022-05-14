def Replace_None(dictionary, replacement):
    for k, v in dictionary.items():
        if isinstance(v, dict):
             Replace_None(v)
        elif v is None:
             dictionary[k] = replacement