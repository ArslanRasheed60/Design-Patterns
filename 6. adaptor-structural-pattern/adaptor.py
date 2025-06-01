# adaptor.py

# Existing interface that clients expect to work with
class USDPaymentSystem:
    """Legacy payment system that only accepts USD"""
    def pay_in_usd(self, amount, currency='USD'):
        if currency.upper() != 'USD':
            print(f"Error: Legacy system only accepts USD, but got {currency}")
            return f"Payment failed: Only USD is accepted"
        return f"Paid ${amount} USD"

# New payment system with a different interface
class MultiCurrencyPaymentSystem:
    """New payment system that supports multiple currencies"""
    def pay(self, amount, currency):
        return f"Paid {amount} {currency}"

# Adapter that makes the new system compatible with the old interface
class PaymentAdapter(USDPaymentSystem):
    """Adapter that makes MultiCurrencyPaymentSystem compatible with USDPaymentSystem"""
    def __init__(self):
        self._multi_currency_system = MultiCurrencyPaymentSystem()
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.92,  # 1 USD = 0.92 EUR
            'GBP': 0.79,  # 1 USD = 0.79 GBP
            'JPY': 150.0  # 1 USD = 150 JPY
        }
    
    def convert_to_usd(self, amount, currency):
        """Convert any currency to USD"""
        return amount / self.exchange_rates.get(currency.upper(), 1.0)
    
    def pay_in_usd(self, amount, currency='USD'):
        """
        Pay using the new system but with the old interface
        Converts any currency to USD before processing
        """
        if currency.upper() != 'USD':
            amount = self.convert_to_usd(amount, currency)
            print(f"Converted {amount} {currency} to {amount} USD")
        return self._multi_currency_system.pay(amount, 'USD')

# Client code
def process_payment(payment_system, amount, currency='USD'):
    """Client code that works with the USDPaymentSystem interface"""
    if currency.upper() != 'USD':
        print(f"Processing {amount} {currency} payment...")
    else:
        print(f"Processing ${amount} payment...")
    
    result = payment_system.pay_in_usd(amount, currency)
    print(f"Result: {result}\n")

# Example usage
if __name__ == "__main__":
    # Using the legacy system (only USD)
    print("=== Legacy System (USD only) ===")
    legacy_system = USDPaymentSystem()
    process_payment(legacy_system, 100)  # Works fine with USD
    
    # This would fail with the legacy system
    # process_payment(legacy_system, 100, 'EUR')  # Would cause an error
    
    # Using the adapter with the new system
    print("\n=== Adapter with Multi-Currency Support ===")
    adapter = PaymentAdapter()
    
    # Now we can use different currencies
    process_payment(adapter, 100)  # USD (no conversion needed)
    process_payment(adapter, 92, 'EUR')  # EUR to USD conversion
    process_payment(adapter, 79, 'GBP')  # GBP to USD conversion
    process_payment(adapter, 15000, 'JPY')  # JPY to USD conversion
