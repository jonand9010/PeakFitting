import numpy as np
from scipy.optimize import curve_fit

class Linear:

    def __init__(self):
        self.parameters = [0, 0]

    def fit(self, x, y):
        
        self.parameters = np.polyfit(x, y, deg = 1)

    def predict(self, x):
        
        y_hat = np.polyval(self.parameters, x)

        return y_hat

class Quadratic:
    def __init__(self):
        self.parameters = [0, 0, 0]

    def fit(self, x, y):
        
        self.parameters = np.polyfit(x, y, deg = 2)

    def predict(self, x, beta0 = None):
        
        y_hat = np.polyval(self.parameters, x)

        return y_hat

class Gaussian:

    def __init__(self, parameters = [0, 0, 0, 0]):
        self.parameters = parameters  

    def model(self, x, amplitude = 1, position = 0, width = 0.1, level = 0):
        
        return amplitude * np.exp(-(x - position)**2 / (2*width) + level)

    def fit(self, x, y, beta0 = [0.7, 0.5, 0.1, 0]):
        
        self.parameters, _ = curve_fit(self.model, x, y, beta0)

    def predict(self, x):

        y_hat =  self.model(x, self.parameters[0], self.parameters[1], self.parameters[2], self.parameters[3])

        return y_hat



class Lorentz:
    
    def __init__(self, parameters = [0, 0, 0, 0]):
        
        self.parameters = parameters  

    def model(self, x, amplitude = 1, position = 0, width = 0.1, level = 0):
        
        return amplitude * width ** 2 / (np.pi * width * ((x - position) ** 2) + width ** 2)

    def fit(self, x, y, beta0 = [0.7, 0.5, 0.1, 0]):
        
        self.parameters, _ = curve_fit(self.model, x, y, beta0)

    def predict(self, x):

        y_hat =  self.model(x, self.parameters[0], self.parameters[1], self.parameters[2], self.parameters[3])

        return y_hat


class PseudoVoigt:

    def __init__(self, parameters = [0, 0, 0, 0, 0.5]):
        self.parameters = parameters  

    def model(self, x, amplitude = 1, position = 0, width = 0.1, level = 0, alpha = 0.5):
        
        return amplitude * ( (1-alpha)/(width * np.sqrt(2*np.pi)) * np.exp(-(x-position)**2 /(2*width**2)) + 
                            alpha/np.pi * (width / ((x - position)**2 + width**2))   ) + level

    def fit(self, x, y, beta0 = [0.7, 0.5, 0.1, 0, 0.5]):
        
        self.parameters, _ = curve_fit(self.model, x, y, beta0)
        
    def predict(self, x):

        y_hat =  self.model(x, self.parameters[0], self.parameters[1], self.parameters[2], self.parameters[3], self.parameters[4])

        return y_hat



