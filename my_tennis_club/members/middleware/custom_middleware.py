# my_app/middleware/custom_middleware.py

from django.http import HttpResponse
from django.shortcuts import redirect


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code yang dijalankan sebelum view dipanggil
        print("Request received: ", request)

        # Lanjutkan ke view yang diminta
        response = self.get_response(request)

        # Code yang dijalankan setelah view dipanggil
        print("Response prepared: ", response)

        return response

    def process_exception(self, request, exception):
        # Menangani exception yang tidak tertangani
        return HttpResponse("Something went wrong!", status=500)
    
class EnsureAuthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path != '/login/':
            return redirect('/login/')
        
        return self.get_response(request)

