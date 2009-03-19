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

Or, put cas_provider somewhere on your Python path.
	
USAGE
======

#. Add ``'cas_consumer'`` to your ``INSTALLED_APPS`` tuple in *settings.py*.
#. In *settings.py*, set ``LOGIN_URL`` to ``'/cas/login/'`` and ``LOGOUT_URL`` to ``'/cas/logout/'``
#. In *urls.py*, put the following line: ``(r'^cas/', include('cas_consumer.urls')),``
