# -*- coding: utf-8 -*-
"""DB-related utilities."""


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD."""

    # TODO: for now, I'm just content about differentiate between the save
    # that actually create new db record and the save that updates fields
    # values of an existing record.
    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()
