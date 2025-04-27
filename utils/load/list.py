class Get_value:

    def with_key(data, key):
        if isinstance(data, dict):
            return data.get(key)
        elif isinstance(data, list):
            values = []
            for item in data:
                if isinstance(item, dict):
                    value = item.get(key)
                    if value is not None:
                        values.append(value)
        return values if values else None


