from marshmallow import fields
from marshmallow import validate, utils
from marshmallow.compat import text_type, basestring

class StringTrim(fields.Field):
    """A string field.

    :param kwargs: The same keyword arguments that :class:`Field` receives.
    """

    default_error_messages = {
        'invalid': 'Not a valid string.'
    }

    def _serialize(self, value, attr, obj):
        if value is None:
            return None
        return utils.ensure_text_type(value.strip())

    def _deserialize(self, value, attr, data):
        if not isinstance(value, basestring):
            self.fail('invalid')
        return utils.ensure_text_type(value.strip())
