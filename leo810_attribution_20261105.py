def total(prices):
    subtotal = sum(prices)
    return round(subtotal, 2)

def add_tax(amount):
    return amount * 1.2

HUMAN_MARKER = "leo810-manual-gap-20261105"

def discounted(amount):
    return amount * 0.9
