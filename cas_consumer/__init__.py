from django.conf import settings

__all__ = []

_DEFAULTS = {
    'CAS_REDIRECT_ON_LOGOUT': '/',
    'CAS_NEXT_DEFAULT': '/',
    'CAS_COMPLETELY_LOGOUT': True,
    'CAS_USERINFO_CALLBACK': None,

    'CAS_SERVICE_LABEL': 'service',
    'CAS_TICKET_LABEL': 'ticket',
    'CAS_EXTRA_LOGIN_PARAMS': {},
    'CAS_EXTRA_VALIDATION_PARAMS': {},

    'CAS_LOGIN_URL': 'login/',
    'CAS_VALIDATE_URL': 'validate/',
    'CAS_LOGOUT_URL': 'logout/',
    'CAS_URLENCODE_PARAMS': True,
}

for key, value in _DEFAULTS.iteritems():
    try:
        getattr(settings, key)
    except AttributeError:
        setattr(settings, key, value)
    except ImportError:
        pass
