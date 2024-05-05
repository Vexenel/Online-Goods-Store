from carts.models import Cart


def get_user_carts(requset):
    if requset.user.is_authenticated:
        return Cart.objects.filter(user=requset.user)
    
    if not requset.session.session_key:
        requset.session.create()
    return Cart.objects.filter(session_key=requset.session.session_key)
    