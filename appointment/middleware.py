# middleware.py
from django.utils.deprecation import MiddlewareMixin

class CurrentUserMiddleware(MiddlewareMixin):
    current_user = None

    def process_request(self, request):
        CurrentUserMiddleware.current_user = request.user

    @classmethod
    def get_current_user(cls):
        return cls.current_user
