from werkzeug.datastructures import ImmutableMultiDict


def immutabledict_to_dict(immutable_dict):
    if not isinstance(immutable_dict, ImmutableMultiDict):
        raise ValueError("Input must be an ImmutableMultiDict")

    return immutable_dict.to_dict()