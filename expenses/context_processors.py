from .models import ExpCoin

def expcoin_balance(request):
    if request.user.is_authenticated:
        try:
            expcoin = ExpCoin.objects.get(user=request.user)
            return {'expcoin_balance': expcoin.balance}
        except ExpCoin.DoesNotExist:
            return {'expcoin_balance': 0}
    return {}
