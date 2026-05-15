class DiscountCalculator:
    def calculate(self, price):
        raise NotImplementedError


class RegularDiscount(DiscountCalculator):
    def calculate(self, price):
        return price * 0.9


class PremiumDiscount(DiscountCalculator):
    def calculate(self, price):
        return price * 0.7


def discounted_cost(type_discount, price):
    return type_discount().calculate(price)


print(discounted_cost(RegularDiscount, 100))  # 90.0
print(discounted_cost(PremiumDiscount, 100))  # 70.0