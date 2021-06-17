import numpy as np
from scipy.optimize import curve_fit
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

    def predict(self, x, beta0 = None):
        
        y_hat = np.polyval(self.param, x)

        return y_hat

class Gaussian:

    def __init__(self, param = [0, 0, 0]):
        self.param = param  

    def Gaussian_model(self, x, amplitude = 1, position = 0, width = 0.1, level = 0):
        
        return amplitude * np.exp(-(x - position)**2 / (2*width) + level)
    
 


    def fit(self, x, y, beta0 = [0.7, 0.5, 0.1, 0]):
        
        self.param, _ = curve_fit(self.Gaussian_model, x, y, beta0)



    def predict(self, x):

        y_hat =  self.Gaussian_model(x, self.param[0], self.param[1], self.param[2])

        return y_hat



class Lorentz:
    pass


class Voigt:
    pass



