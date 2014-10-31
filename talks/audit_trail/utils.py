IGNORE_FIELDS = ['password', 'id']


def compare_dicts(new, old):
    """Compare the values of two dict
    :param new: dict containing latest values
    :param old: dict containing previous values
    :return dict containing tuples (new value, old value, bool changed)
    """
    diff = {}
    for k, v in new.iteritems():
        if k not in IGNORE_FIELDS:
            diff[k] = v
    if old:
        for k, v in old.iteritems():
            if k not in IGNORE_FIELDS:
                if k in diff:
                    new_value = diff[k]
                    changed = new_value != v
                    diff[k] = (new_value, v, changed)
                else:
                    diff[k] = (None, v, False)
    else:
        for k, v in diff.iteritems():
            diff[k] = (v, None, False)
    return diff


def find_user_friendly_rel(field, value):
    """Try to find a value from a lookup table
    for a given field
    :param field: django db field to introspect
    :param value: PK value
    :return string representation of the value
    """
    if value:
        obj = field.rel.to.objects.get(id=value)
        if hasattr(obj, 'text'):
            return obj.text
        elif hasattr(obj, 'name'):
            return obj.name
        else:
            return str(obj)
    else:
        return value


def find_user_friendly_many(field, values):
    """Try to find values of a many to many
    :param field: django db field to introspect
    :param values: PK values
    :return string representation of all the values
    """
    if values:
        texts = []
        for value in values:
            texts.append(find_user_friendly_rel(field, value))
        return ', '.join(texts)
    else:
        return None


def find_user_friendly_display_name(field, value):
    """Try to find the user friendly name for a field with
    a list of choices
    :param field: django db field to introspect
    :param value: stored value from an enumeration
    :return friendly value from the enumeration else original value
    """
    for key, friendly_name in field.choices:
        if key == value:
            return friendly_name
    return value
