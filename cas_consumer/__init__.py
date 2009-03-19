from django.conf import settings

__all__ = []

_DEFAULTS = {
    'CAS_SERVICE': 'http://127.0.0.1/cas/login/',
    'CAS_BASE': 'http://127.0.0.2/cas/',
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
