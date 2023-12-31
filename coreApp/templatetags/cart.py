from django import template

register = template.Library()


@register.filter(name='inTheCart')
def inTheCart(prod, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == prod:
            return True
    return False

@register.filter(name='prodQuantity')
def prodQuantity(prod, cart):
    keys = cart.keys()
    for row in keys:
        if int(row) == prod:
            return cart.get(row)['quantity']
    return 0

@register.filter(name='prodTotal')
def prodTotal(prod, cart):
    q = prodQuantity(prod.id, cart)
    itemTotal = int(prod.price) * int(q)
    print('itemTotal', itemTotal)
    print('prodTotal', prod.price, q)
    return itemTotal

@register.filter(name='cartTotal')
def cartTotal(prods, cart):
    sum = 0
    print('sum pre loop in tag', sum)
    count = 0
    for prod in prods:
        sum += int(prodTotal(prod, cart))
        print('sum in tag loop', sum)
    theTotal = f'${sum}'
    return theTotal