from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from django.views.generic import TemplateView

class Home(TemplateView):
      template_name = 'index.html'

      def get(self, request):
          ctx = {}
          return render(request, self.template_name, {})
