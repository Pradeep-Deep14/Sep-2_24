def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

# Example usage
nested_dict = {
    'a': 1,
    'b': {'c': 2, 'd': {'e': 3, 'f': 4}},
    'g': 5
}

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)
