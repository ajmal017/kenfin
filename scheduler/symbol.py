class Symbol(object):
    def __init__(self, symbol, configurator):
        self.symbol = symbol["symbol"]
        self.configurator = configurator
        self.model = self.load_model(self.symbol)
        self.data = self.load_data(self.symbol)

    def load_model(self, symbol):
        return "loaded model from pkl file"

    def symbol_action(self):
        print("Symbol loaded %s" % self.symbol)

    def load_data(self, symbol):
        return "loaded daily data in the morning"
