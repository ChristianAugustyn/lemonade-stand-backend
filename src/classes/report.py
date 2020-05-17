from products.models import Product
from staff.models import StaffMember
from decimal import Decimal

class ReportItem:
    def __init__(self, staff_member, date, orders):
        self.staff_member = staff_member
        self.date = date
        self.orders = orders
        self.total_price = self.getTotalPrice()
        self.items = self.getItems()
        self.commission = self.getCommission()

    
    def getTotalPrice(self):
        total = 0
        for order in self.orders:
            total += Decimal(Product.objects.get(id=int(order.item_id)).price)

        return total

    def getCommission(self):
        return self.getTotalPrice() * (self.staff_member.commission / 100)

    def getItems(self):
        items = []
        for order in self.orders:
            items.append(Product.objects.get(id=int(order.item_id)).name)
        
        return ', '.join(items)