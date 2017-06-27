

class AttrsConvertException:
	pass


def dump(attrs_obj):
	"""
	Converts attrs data into unstructred data with basic types, recursively.

	 - attrs classes => dictionaries
        - Enumeration => values
        - Other types are let through without conversion,
          such as, int, boolean, dict, other classes.
	"""
	pass


def load(model, value):
	"""
	Converts unstructrued data into attrs class based on model, recursively.
	"""
	pass


def _dump(obj):
	pass


def _dump_attrs(obj):
	pass


def _dump_enum(obj):
	pass

def _dump_set(obj):
	pass

def _dump_sequence(obj):
	# list, tuple, range
	pass


def _dump_dict(obj):
	pass


def _dump_default(obj):
	return obj


## Small Helper Functions
def _is_attrs_class(cls):
    try:
        attrs = getattr(cls, "__attrs_attrs__", None)
    except Exception:
        return False
    return attrs is not None


def _get_attributes(attrs_obj):
	return getattr(attrs_obj, "__attrs_attrs__", None)


def _get_values(attrs_obj):
	return getattr(attrs_obj, "__dict__")
