===================
django-cas-consumer
===================

---------------------------------
Chris Williams <chris@nitron.org>
---------------------------------

OVERVIEW
=========

django-cas-provider is a consumer for the `Central Authentication
Service <http://jasig.org/cas>`_. It supports CAS version 1.0. It allows
remote services to authenticate users for the purposes of
`Single Sign-On (SSO) <http://en.wikipedia.org/wiki/Single_Sign_On>`_. For
example, a user logs into a CAS server (provided by django-cas-provider) and
can then access other services (such as email, calendar, etc) without
re-entering her password for each service. For more details, see the
`CAS wiki <http://www.ja-sig.org/wiki/display/CAS/Home>`_.
It is meant to be used alongside `django-cas-provider <http://nitron.org/projects/django-cas-provider/>`_.

INSTALLATION
=============

To install, run the following command from this directory:

    	``python setup.py install``

Or, put cas_consumer somewhere on your Python path.

USAGE
======

#. Add ``'cas_consumer'`` to your ``INSTALLED_APPS`` tuple in *settings.py*.
#. In *settings.py*, set ``LOGIN_URL`` to ``'/cas/login/'`` and ``LOGOUT_URL`` to ``'/cas/logout/'``
#. In *settings.py*, set the CAS_* settings (detailed below).
#. In *urls.py*, put the following line: ``(r'^cas/', include('cas_consumer.urls')),``
#. Add ``'cas_consumer.backends.CASBackend'`` to your ``AUTHENTICATION_BACKENDS`` tuple in *settings.py*

SETTINGS
========

- *CAS_BASE*: The base URL of the CAS provider. Example: ``'http://provider.com/cas/'``. No default.
- *CAS_SERVICE*: The "service" URL to report to the provider. Example: ``'http://example.com/cas/login/'``. No default.
- *CAS_NEXT_DEFAULT*: URL to redirect to after successful login. Example (default): ``'/'``
- *CAS_COMPLETELY_LOGOUT*: Boolean. If True, the CAS provider will be notified of logout. Default: True
- *CAS_REDIRECT_ON_LOGOUT*: URL to redirect to after logout. Example (default): ``'/'``
- *CAS_USERINFO_CALLBACK* (optional): Python callable that retrieves full name, email, etc from an external source. Default: None

OTHER SETTINGS
--------------

For non-standard CAS implementations, it's sometimes necessary to fudge on a few of the details. These settings allow you to do that.

- *CAS_SERVICE_LABEL*: Name of the GET variable carrying the service info. Defaults to ``service``
- *CAS_TICKET_LABEL*: Name of the GET variable carrying the ticket info. Defaults to ``ticket``
- *CAS_EXTRA_LOGIN_PARAMS*: Dictionary of extra params that need to be passed to the server on a login request.
- *CAS_EXTRA_VALIDATION_PARAMS*: Dictionary of extra params that need to be passed to the server on ticket validation.
- *CAS_LOGIN_URL*: The url, relative to the CAS_BASE, where login requests to the server should be made. Defaults to ``login/`` (notice the lack of a leading slash)
- *CAS_VALIDATE_URL*: The url, relative to the CAS_BASE, where validation requests to the server should be made. Defaults to ``validate/`` (notice the lack of a leading slash)
- *CAS_URLENCODE_PARAMS*: Whether or not to use url encoding when making requests to the server. This is to address server implementations that don't properly url encode their data and don't expect url-encoded data. Defaults to ``True`` obviously, as not url-encoding breaks any data with special characters.

CAS_USERINFO_CALLBACK
=====================

Example::

    def getUserInfo(user):
        """ Calls getFirstName, getLastName, getEmail, which call
            a remote service to get that information.
            Their implementations are not important for this
            example.
        """
        user.first_name = getFirstName(user.username)
        user.last_name = getLastName(user.username)
        user.email = getEmail(user.username)
        user.save()

In settings.py::

    from your_app.helpers import getUserInfo
    CAS_USERINFO_CALLBACK = getUserInfo

Servers requiring a specific ordering of parameters
===================================================

Some CAS server implementations require that GET variables arrive in a specific order. In that case, the ``CAS_EXTRA_LOGIN_PARAMS`` and ``CAS_EXTRA_VALIDATION_PARAMS`` dictionaries can be used to enforce that order by using ordered dictionary classes. For example, to enforce a specific ordering of parameters on the validation request to the server (along with adding an extra parameter), you could define the following in you ``settings.py`` ::

	from odict import odict

	CAS_EXTRA_VALIDATION_PARAMS = odict((
		('cassvc', 'IU'),
		(CAS_TICKET_LABEL, None),
		(CAS_SERVICE_LABEL, None)))

The ``odict`` package can be installed via pypi and can also be found via the `Plone Archetypes SVN repo <https://svn.plone.org/svn/archetypes/AGX/odict/>`_. Any Class that implements both the update() and items() ``dict` methods should work though.