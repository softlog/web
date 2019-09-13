from sqlalchemy.types import TypeDecorator
from app import db

class StrippedString(TypeDecorator):

    impl = db.String

    def process_bind_param(self, value, dialect):
        # In case you have nullable string fields and pass None
        print(value)
        return value.strip() if value else value

    def copy(self, **kw):
        return StrippedString(self.impl.length)