# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from pymos.database import CRUDMixin
from pymos.extensions import bcrypt, db


class User(UserMixin, db.Document, CRUDMixin):
    """A user of the app."""

    username = db.StringField(
        unique=True,
        required=True,
    )
    email = db.EmailField(
        unique=True,
        required=True,
    )
    #: The hashed password
    password = db.StringField(
        required=True,
    )
    created_at = db.DateTimeField(
        required=True,
        default=dt.datetime.utcnow,
    )
    first_name = db.StringField()
    last_name = db.StringField()
    active = db.BooleanField(
        default=False,
    )
    is_admin = db.BooleanField(
        default=False,
    )

    # def __init__(self, username, email, password=None, **kwargs):
    #     """Create instance."""
    #     db.Document.__init__(self, username=username, email=email, **kwargs)
    #     # if password:
    #     #     self.set_password(password)
    #     # else:
    #     #     self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f'<User({self.username})>'


class Role(db.Document):
    """An access role that a user can have."""

    name = db.StringField(
        unique=True,
        required=True,
    )
    users = db.ListField(
        db.ReferenceField(User),
    )

    def __repr__(self):
        """Represent instance as a unique string."""
        return f'<Role({self.name})>'
