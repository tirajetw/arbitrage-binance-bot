from binance.client import Client
from binance.enums import *
import time
import os
from datetime import datetime
import matplotlib
from matplotlib import cm
import matplotlib.pyplot as plt
from binance.enums import *
import pprint
import math
from BinanceKeys import BinanceKey1
import decimal

"""BINANCE API"""
api_key = BinanceKey1['api_key']
api_secret = BinanceKey1['api_secret']

client = Client(api_key, api_secret)
print(client)

def run():
    os.system('cls')
    while 1:
        try:
            initialize()

        except:
            print("(!) Fail to run\n\n")
            break

def float_to_str(f):
    """
    Convert the given float to a string,
    without resorting to scientific notation
    """
    ctx = decimal.Context()
    ctx.prec = 20
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')

def initialize():
    