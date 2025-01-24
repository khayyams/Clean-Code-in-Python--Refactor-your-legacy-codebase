from abc import ABC, abstractmethod


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
    

class PaymentProcessor(ABC):
    @abstractmethod
    def sms_authentication(self, code) -> None:
        pass

    @abstractmethod
    def pay(self, order) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code) -> None:
        super().__init__()
        self.security_code = security_code
        self.verified = False


    def sms_authentication(self, code) -> None:
        print(f'Verifying SMS code {code}')
        self.verified = True
    
    def pay(self, order) -> None:
        if not self.verified:
            raise Exception('Not authorised')
        print('Processing debit type...')
        print(f'Verifynig security code: {self.security_code}')
        order.status = 'paid'


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code) -> None:
        super().__init__()
        self.security_code = security_code
    
    def sms_authentication(self, code) -> None:
        raise Exception('Credit card payment doesn\'t support SMS code authentication!')
    
    def pay(self, order) -> None:
        print('Processing credit type...')
        print(f'Verifynig security code: {self.security_code}')
        order.status = 'paid'


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address) -> None:
        super().__init__()
        self.email_address = email_address
        self.verified = False


    def sms_authentication(self, code) -> None:
        print(f'Verifying SMS code {code}')
        self.verified = True
    
    def pay(self, order) -> None:
        if not self.verified:
            raise Exception('Not authorised')
        print('Processing paypal type...')
        print(f'Verifynig email address: {self.email_address}')
        order.status = 'paid'

        
order = Order()
order.add_item('Keyboard', 1, 50)
order.add_item('SSD', 1, 150)
order.add_item('Lipstick', 2, 70)

print('Total price: ', order.total_price())
payment = PaypalPaymentProcessor('harash@perfect.team')
payment.pay(order)
