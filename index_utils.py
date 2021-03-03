def is_valid_axis_range(axis):
    """Determines if a value is a valid axis range.
    
    A valid index is a tuple that is one of:
        - int
        - slice
        - list composes of ints and slices
    """
    if isinstance(axis, int):
        return True
    elif isinstance(axis, slice):
        return True
    elif isinstance(axis, list):
        for v in axis:
            if not (isinstance(v, int) or isinstance(v, slice)):
                return False
        return True
    return False


def is_valid_index_range(index, dimension=3):
    """Determines if a value is a valid index range.

    A valid index is a tuple that:
        - len(self) == dimension of the space
        - all elements are valid axis ranges
    """

    if not (isinstance(index, tuple) and len(index)==3):
        return False

    for ax in index:
        if not is_valid_axis_range(ax):
            return False
    return True


def is_in_slice(value, s):
    start = s.start
    stop = s.stop
    step = s.step
    if (start is None) and (stop is None) and (step is None):
        return True
    elif (start is not None) and (stop is None) and (step is None):
        return start <= value
    elif (start is None) and (stop is not None) and (step is None):
        return value < stop
    elif (start is not None) and (stop is not None) and (step is None):
        return start <= value < stop
    elif (start is None) and (stop is None) and (step is not None):
        raise ValueError('Either start or stop mush be given when step is given.')
    elif (start is not None) and (stop is None) and (step is not None):
        return start <= value and (value-start)%step == 0
    elif (start is None) and (stop is not None) and (step is not None):
        return value < stop and (value-stop)%step == 0
    elif (start is not None) and (stop is not None) and (step is not None):
        return start <= value < stop and (value-start)%step == 0
    return False

def is_in_axis_range(position, axis):
    """Determines if a position is in the index range.

    The position is in the index range if
    all values of the position on every axis are in the axis ranges of the index range on the corresponding axis.
    """
    if not is_valid_axis_range(axis):
        raise TypeError

    if isinstance(axis, int):
        return position == axis
    if isinstance(axis, slice):
        return is_in_slice(position, axis)
    if isinstance(axis, list):
        for a in axis:
            if isinstance(a, int):
                if position == a:
                    return True
            if isinstance(a, slice):
                if is_in_slice(position, a):
                    return True
    return False


def is_in_index_range(value, index):
    """Determines if a value is in the index range.

    The value is in the axis range if one of:
        - axis is int and value == axis
        - axis is a slice and value is in that slice. See is_in_slice for detail.
        - axis is a list and value is in any of the elements.
    """
    for v, a in zip(value, index):
        if not is_in_axis_range(v, a):
            return False
    return True
