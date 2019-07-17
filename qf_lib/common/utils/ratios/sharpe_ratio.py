import numpy as np

from qf_lib.common.enums.frequency import Frequency
from qf_lib.common.utils.returns.cagr import cagr
from qf_lib.common.utils.volatility.get_volatility import get_volatility
from qf_lib.containers.series.qf_series import QFSeries


def sharpe_ratio(qf_series: QFSeries, frequency: Frequency, risk_free: float=0) -> float:
    """
    Calculates the Sharpe Ratio for a given timeseries of returns and given frequency.

    Parameters
    ----------
    qf_series
        financial series
    frequency
        frequency of the series
    risk_free
        risk free rate

    Returns
    -------
    sharpe_ratio
        Sharpe Ratio for given series and frequency
    """
    annual_simple_return = cagr(qf_series, frequency)
    annual_log_return = np.log(annual_simple_return + 1)
    annual_vol = get_volatility(qf_series, frequency, annualise=True)

    return (annual_log_return - risk_free) / annual_vol
