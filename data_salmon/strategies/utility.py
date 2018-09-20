
def check_min_max(field):
    if field.min == None or field.max == None:
        raise ValueError('Missing value: min={}, max={}'.format(
            field.min, field.max))

    if field.min > field.max:
        raise ValueError('Min is larger than max! min={}, max={}'.format(
            field.min, field.max))

def check_increment(field):
    if field.increment == None:
        raise ValueError(
            'Missing value: increment={}'.format(field.increment))