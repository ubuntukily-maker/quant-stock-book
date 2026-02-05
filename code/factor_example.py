import pandas as pd

def momentum_factor(price, window=20):
    """
    动量因子（Momentum Factor）
    """
    return price / price.shift(window) - 1
