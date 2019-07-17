from datetime import datetime

import matplotlib.pyplot as plt

from demo_scripts.demo_configuration.demo_ioc import container
from qf_lib.common.enums.price_field import PriceField
from qf_lib.common.tickers.tickers import QuandlTicker
from qf_lib.data_providers.general_price_provider import GeneralPriceProvider
from qf_lib.plotting.helpers.create_returns_similarity import create_returns_similarity

start_date = datetime(2016, 1, 1)
end_date = datetime(2018, 1, 1)
live_start_date = datetime(2017, 1, 1)


def main():
    data_provider = container.resolve(GeneralPriceProvider)
    spy_tms = data_provider.get_price(QuandlTicker('AAPL', 'WIKI'), PriceField.Close, start_date, end_date)

    first_part = spy_tms.loc[spy_tms.index < live_start_date]
    first_part.name = 'first part of series'

    last_part = spy_tms.loc[spy_tms.index > live_start_date]
    last_part.name = 'last part of series'

    returns_similarity_chart = create_returns_similarity(
        first_part, last_part, mean_normalization=False, std_normalization=False, )
    returns_similarity_chart.plot()
    plt.show(block=True)


# Note: there was a bug in the sklearn library, which might cause this script to fail.


if __name__ == '__main__':
    main()
