from matplotlib.pyplot import hist
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
        period=2,
        frequency_type='daily',
        frequency=1,
        extended_hours=False
    )
    pprint.pprint(VIX_His)

    VXX_His = td_session.get_price_history(
        symbol='VXX',
        period_type='year',
        period=2,
        frequency_type='daily',
        frequency=1,
        extended_hours=False
    )
    pprint.pprint(VXX_His)


if __name__ == '__main__':
    main()