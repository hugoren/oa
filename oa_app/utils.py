from functools import wraps
from django.http import HttpResponseRedirect


def log_in_check(f):
    @wraps(f)
    def check(*args, **kwargs):
        try:
            user = args[0].user
            if user.is_authenticated and user.is_active:
                    return f(*args, **kwargs)
            else:
                return HttpResponseRedirect('/login')
        except Exception as e:

            print(e)

    return check
