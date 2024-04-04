import json


class CurrencyRateManager:
    def __init__(self, filename='currency_rates.json'):
        self.filename = filename
        self.rates = self.load_currency_rates()

    def save_currency_rates(self):
        with open(self.filename, 'w') as file:
            json.dump(self.rates, file, indent=2)

    def load_currency_rates(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def update_currency_rate(self, currency_code, rate):
        self.rates[currency_code] = rate
        self.save_currency_rates()
        print(f"Currency rate for {currency_code} updated to {rate}.")

    def get_currency_rate(self, currency_code):
        if currency_code in self.rates:
            return self.rates[currency_code]
        else:
            print(f"Currency rate for {currency_code} not found.")
            return None