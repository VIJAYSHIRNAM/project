def immutable_to_dict(data):
    return {key : data.getlist(key) for key in data.to_dict()}