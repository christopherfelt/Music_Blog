from django.contrib.auth import logout
from django.views.generic import View
from django.http import HttpResponseRedirect


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

