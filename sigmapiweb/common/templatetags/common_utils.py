"""
Utility functions available to all SigmaPi templates.
"""

from django import template

from ..utils import get_full_name_or_deleted


register = template.Library()


@register.filter
def full_name(model, user_field_name):
    """
    Safely get the full name of user field on a model.

    Arguments:
        model (django.models.Model)
        user_field_name (str): Name of user field on model

    Returns: str
        Either the full name, or '[deleted]' if the user is None
        or not a field on model.
    """
    return get_full_name_or_deleted(
        getattr(model, user_field_name, None)
    )