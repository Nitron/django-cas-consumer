from django.conf import settings

__all__ = []

_DEFAULTS = {
    'CAS_REDIRECT_ON_LOGOUT': '/',
    'CAS_NEXT_DEFAULT': '/',
    'CAS_COMPLETELY_LOGOUT': True,
}

for key, value in _DEFAULTS.iteritems():
    try:
        getattr(settings, key)
    except AttributeError:
        setattr(settings, key, value)
    except ImportError:
        pass
