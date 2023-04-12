import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 440942058 # Ваш chat ID, не меняйте название переменной

//def solution(p: float, x: np.array) -> tuple:
//    # Измените код этой функции
//    # Это будет вашим решением
//    # Не меняйте название функции и её аргументы
//    alpha = 1 - p
//    loc = x.mean() - 0.005
//    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
//    return loc - scale * norm.ppf(1 - alpha / 2), \
//           loc - scale * norm.ppf(alpha / 2)

def solution(p, x):
    alpha = 1 - p
    t = x.max() - 0.005
    n = len(x)
    return 0.005 + t / ((1 - alpha / 2)**(1 / n)), \
           0.005 + t / ((alpha / 2)**(1 / n))
