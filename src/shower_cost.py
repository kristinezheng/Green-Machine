import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time, datetime
import requests
import regex as re

def convert_request_to_price(t):
    if t == '\n':
        return []
    u = t.partition(',')
    return [u[0]] + convert_request_to_price(u[2])

def tz_from_utc_ms_ts(utc_ms_ts, tz_info):
    """Given millisecond utc timestamp and a timezone return datetime

    :param utc_ms_ts: Unix UTC timestamp in milliseconds
    :param tz_info: timezone info
    :return: timezone aware datetime
    """
    # convert from time stamp to datetime
    utc_datetime = datetime.datetime.utcfromtimestamp(utc_ms_ts / 1000.)
    # set the timezone to UTC, and then convert to desired timezone
    return utc_datetime.replace(tzinfo=pytz.timezone('UTC')).astimezone(tz_info)

def convert_millis_data(t): 
    price_dict = {}
    p = convert_request_to_price(t)
    for i in p: 
        part = i.partition(':')
        price_dict[pd.to_datetime(tz_from_utc_ms_ts(int(part[0]), pytz.timezone('America/New_York'))).tz_localize(None)] = part[2]
    df = pd.DataFrame.from_dict(price_dict, orient='index', columns=['Price']).rename_axis('TimeStamp').reset_index()
    return df, price_dict #in local time
  
def return_current_price():
    def convert_current_price(data):
        pattern = "\"price\":\"(.*?)\""
        return float(re.search(pattern, data).group(1))

    url = 'https://hourlypricing.comed.com/api?type=currenthouraverage'
    r = requests.get(url)
    data = r.text
    
    return convert_current_price(data)

def return_price_history(start, end):
  start, end = time.strftime('%Y%m%d%H%M', start), time.strftime('%Y%m%d%H%M', end)
  url = 'https://hourlypricing.comed.com/api?type=5minutefeed&datestart=%s&dateend=%s&format=text' % (start, end)
  r = requests.get(url)
  data = r.text
  df, d = convert_millis_data(data)
  return d

