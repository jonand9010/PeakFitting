import numpy as np

class Linear:
    def __init__(self):
        self.param = [0, 0]

    def fit(self, x, y):
        
        self.param = np.polyfit(x, y, deg = 1)

    def predict(self, x):
        
        y_hat = np.polyval(self.param, x)

        return y_hat

class poly2:
    def __init__(self):
        self.param = [0, 0, 0]

    def fit(self, x, y):
        
        self.param = np.polyfit(x, y, deg = 2)

    def predict(self, x):
        
        y_hat = np.polyval(self.param, x)

        return y_hat

class Gaussian:
    pass


class Lorentz:
    pass


class Voigt:
    pass