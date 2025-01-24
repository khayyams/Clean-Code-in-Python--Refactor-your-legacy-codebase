class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self) -> float:
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    def pay(self, payment_type, security_code) -> None:
        if payment_type == 'debit':
            print('Processing debit type...')
            print(f'Verifynig security code: {security_code}')
            self.status = 'paid'
        elif payment_type == 'credit':
            print('Processing credit type...')
            print(f'Verifynig security code: {security_code}')
            self.status = 'paid'
        else:
            raise Exception(f'Unknown payment type: {payment_type}')
        
order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('Lipstick', 2, 70)

print('Total price: ', order.total_price())
order.pay('debit', '123456')
