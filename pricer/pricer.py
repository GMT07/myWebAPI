# coding: utf-8


# Librairies
from math import *
from numpy import sqrt, log
from utils import utils


def option_price_monte_carlo(option_type, S, K, T, r, V, nSimulations):
    """Computes the option price with the Monte Carlo method.

        Returns a option price with the Monte Carlo method
        :param option_type: option type : call or put
        :param S: spot or underlying price
        :param K: exercise price
        :param r: interest rate
        :param V: volatility of underlying
        :param T: time to maturity of option
        :return: option price
        """

    drift = (r - (V*V / 2)) * T
    vSqrdt = V * sqrt(T)
    running_sum, this_payoff = 0.0, 0.0
    for i in range(1, nSimulations):
        gauss = utils.gauss1()
        this_spot = S*exp(drift + vSqrdt*gauss)
        if option_type.upper() == "CALL":
            this_payoff = max(this_spot - K, 0.0)
        elif option_type.upper() == "PUT":
            this_payoff = max(K - this_spot, 0.0)

        running_sum += this_payoff

    mean = running_sum / nSimulations
    mean = mean * exp(-r * T)

    return mean


def option_price_black_scholes(option_type, spot, strike, risk_free, sigma, maturity):
    """Computes the option price with the Black Scholes formula.

    Returns a option price with the Black-Scholes formula
    :param option_type: option type : call or put
    :param spot: spot or underlying price
    :param strike: exercise price
    :param risk_free: interest rate
    :param sigma: volatility of underlying
    :param maturity: time to maturity of option
    :return: option price
    """

    time_sqrt = sqrt(maturity)
    d1 = (log(spot/strike)+risk_free*maturity)/(sigma*time_sqrt)+0.5*sigma*time_sqrt
    d2 = d1 - (sigma*time_sqrt)

    if option_type.upper() == "CALL":
        return spot * utils.pgaussred(d1) - strike*exp(-risk_free*maturity) * utils.pgaussred(d2)
    elif option_type.upper() == "PUT":
        return strike*exp(-risk_free*maturity) * utils.pgaussred(-d2) - spot * utils.pgaussred(-d1)



