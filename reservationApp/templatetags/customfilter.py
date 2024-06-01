from atexit import register
from django import template
from cryptography.fernet import Fernet
from django.conf import settings


register = template.Library()

@register.filter
def replaceBlank(value,stringVal = ""):
    value = str(value).replace(stringVal, '')
    return value

@register.filter
def encryptdata(value):
    fernet = Fernet(settings.ID_ENCRYPTION_KEY)
    value = fernet.encrypt(str(value).encode())
    return value

@register.filter
def changeToFalse(val):
    return False

@register.filter
def changeToTrue(val):
    return True


@register.filter
def modTen(val):
    return val%10


@register.filter
def get_location_flag(via_locations, location_id):
    # Ensure via_locations is an iterable (like a list or set) of IDs
    return location_id in via_locations
