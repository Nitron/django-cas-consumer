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

__all__ = ['login', 'profile', 'register', 'logout',]

service = settings.CAS_SERVICE
cas_base = settings.CAS_BASE
cas_login = cas_base + 'login/'
cas_validate = cas_base + 'validate/'
cas_logout = cas_base + 'logout/'
cas_next_default = settings.CAS_NEXT_DEFAULT

def login(request):
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
        
def logout(request, next_page=None):
    auth_logout(request)
    if settings.CAS_COMPLETELY_LOGOUT:
        return HttpResponseRedirect('%s?url=%s' % (cas_logout, 'http://127.0.0.1'))
    return HttpResponseRedirect('/')
