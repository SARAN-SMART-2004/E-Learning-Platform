from django.core.exceptions import PermissionDenied
from functools import wraps


def teacher_required(view_func):
    """
    Decorator to restrict access to views for only users with status of 'tutor'.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.status == 'tutor':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied("You do not have permission to access this page.")
    return _wrapped_view
