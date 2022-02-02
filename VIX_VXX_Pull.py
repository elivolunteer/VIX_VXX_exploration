import csv
from config import CONSUMER_KEY, REDIRECT_URI, TD_ACCOUNT
import datetime as dt
import matplotlib as plt
import numpy
import pandas
import pprint
from td.client import TDClient

def main():

    # Create a new instance of the client
    td_session = TDClient(client_id = CONSUMER_KEY, 
                        redirect_uri = REDIRECT_URI, 
                        credentials_path='credentials.json')

    # Login to a new session
    td_session.login()
    if (td_session):
        print(f'*****************Successfully started session*****************')
    else:
        print(f'Failed to connect to session. Try reauthenticating')


    VIX_His = td_session.get_price_history(
        symbol='$VIX.X',
        period_type='year',
        period=3,
        frequency_type='daily',
        frequency=1,
        extended_hours=False
    )

    VXX_His = td_session.get_price_history(
        symbol='VXX',
        period_type='year',
        period=3,
        frequency_type='daily',
        frequency=1,
        extended_hours=False
    )

    # Saving
    csv_columns = ["close", "datetime", "high", "low", "open", "volume"]
    with open("data/VIX_His.csv", 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for candle in VIX_His["candles"]:
            writer.writerow(candle)
    with open("data/VXX_His.csv", 'w') as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        for candle in VXX_His["candles"]:
            writer.writerow(candle)

if __name__ == '__main__':
    main()