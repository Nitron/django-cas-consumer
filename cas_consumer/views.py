from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.exceptions import SuspiciousOperation
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.conf import settings

__all__ = ['login', 'logout',]

service = settings.CAS_SERVICE
cas_base = settings.CAS_BASE
cas_login = cas_base + 'login/'
cas_validate = cas_base + 'validate/'
cas_logout = cas_base + 'logout/'
cas_next_default = settings.CAS_NEXT_DEFAULT
cas_redirect_on_logout = settings.CAS_REDIRECT_ON_LOGOUT

def login(request):
	""" Fairly standard login view.

		1. Checks request.GET for a service ticket.
        2. If there is NOT a ticket, redirects to the CAS provider's login page.
        3. Otherwise, attempt to authenticate with the backend using the ticket.
        4. If the backend is able to validate the ticket, then the user is logged in and redirected to *CAS_NEXT_DEFAULT*.
        5. Otherwise, the process fails and displays an error message.

	"""
    ticket = request.GET.get('ticket', None)
    next = request.GET.get('next_page', cas_next_default)
    if ticket is None:
        return HttpResponseRedirect('%s?service=%s' % (cas_login, service))
    user = authenticate(service=service, ticket=ticket)
    if user is not None:
        auth_login(request, user)
        name = user.first_name or user.username
        message ="Login succeeded. Welcome, %s." % name
        user.message_set.create(message=message)
        return HttpResponseRedirect(cas_next_default)
    else:
        return HttpResponseForbidden("Error authenticating with CAS")
        
def logout(request, next_page=cas_redirect_on_logout):
    """ Logs the current user out. If *CAS_COMPLETELY_LOGOUT* is true, redirect to the provider's logout page,
        which will redirect to ``next_page``.

    """
    auth_logout(request)
    if settings.CAS_COMPLETELY_LOGOUT:
        return HttpResponseRedirect('%s?url=%s' % (cas_logout, next_page))
    return HttpResponseRedirect(cas_redirect_on_logout)
