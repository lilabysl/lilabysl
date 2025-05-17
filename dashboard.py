#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 12 17:49:25 2025

@author: aishaoyebanji
"""

from alpha_vantage.timeseries import TimeSeries

api_key = 'X8B2MCSBGWTYRIMU'
ts = TimeSeries(key=api_key, output_format='pandas')

data, meta_data = ts.get_quote_endpoint(symbol='AAPL')
print(data)

from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'X8B2MCSBGWTYRIMU'
ts = TimeSeries(key=api_key, output_format='pandas')

while True:
    data, _ = ts.get_quote_endpoint(symbol='AAPL')
    price = data['05. price'].iloc[0]
    print(f"Current AAPL Price: ${price}")
    time.sleep(5)  # refresh every 10 seconds
    
    
print("Running script...")
    