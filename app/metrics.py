from django.utils.formats import number_format
from products.models import Product


def get_product_metrics():

    products = Product.objects.all()
    total_cost_price = sum(p.cost_price * p.quantity for p in products)
    total_selling_price = sum(p.selling_price * p.quantity for p in products)
    total_quantity = sum(p.quantity for p in products)
    total_profit = sum((p.selling_price - p.cost_price) * p.quantity for p in products if p.selling_price and p.cost_price)

    return {
        'total_cost_price': number_format(total_cost_price, decimal_pos=2, force_grouping=True),
        'total_selling_price': number_format(total_selling_price, decimal_pos=2, force_grouping=True),
        'total_quantity': total_quantity,
        'total_profit': number_format(total_profit, decimal_pos=2, force_grouping=True),
    }
