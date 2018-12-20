from abc import ABCMeta, abstractmethod

from qf_lib.backtesting.broker.broker import Broker
from qf_lib.backtesting.contract_to_ticker_conversion.base import ContractTickerMapper
from qf_lib.backtesting.data_handler.data_handler import DataHandler
from qf_lib.backtesting.events.notifiers import Notifiers
from qf_lib.backtesting.monitoring.abstract_monitor import AbstractMonitor
from qf_lib.backtesting.order.orderfactory import OrderFactory
from qf_lib.backtesting.position_sizer.position_sizer import PositionSizer
from qf_lib.common.utils.dateutils.timer import Timer
from qf_lib.data_providers.price_data_provider import DataProvider
from qf_lib.settings import Settings


class TradingSession(object, metaclass=ABCMeta):
    """
    Base class for all Trading Sessions. It configures all the elements of the trading environment.
    """

    def __init__(self):
        self.trading_session_name = None    # type: str
        self.settings = None                # type: Settings
        self.data_provider = None           # type: DataProvider

        self.timer = None                   # type: Timer
        self.data_handler = None            # type: DataHandler
        self.monitor = None                 # type: AbstractMonitor
        self.broker = None                  # type: Broker

        self.contract_ticker_mapper = None  # type: ContractTickerMapper
        self.order_factory = None           # type: OrderFactory
        self.position_sizer = None          # type: PositionSizer

        self.notifiers = None               # type: Notifiers


    @abstractmethod
    def start_trading(self) -> None:
        """
        Run this method in order to perform historical backtest
        """