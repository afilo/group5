from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
User = get_user_model()

def employee_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login'):
    '''
    Decorator for views that checks that the logged in user is an employee,
    redirecting to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_employee,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/admin'):
    '''
    Decorator for views that checks that the logged in user is an admin,
    redirecting to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def client_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login'):
    '''
    Decorator for views that checks that the logged in user is a client,
    redirecting to the log-in page if necessary.
    '''
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_client,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator