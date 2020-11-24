def transfer_data_list(data, func):
    """Recursively do transformation."""
    try:
        temp = []
        for x in data:
            temp.append(transfer_data_list(x, func))
        return temp
    except:
        return func(data)
