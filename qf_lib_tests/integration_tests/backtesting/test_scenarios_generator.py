import unittest
from unittest import TestCase

import pandas as pd

from qf_lib.backtesting.fast_alpha_model_tester.scenarios_generator import ScenariosGenerator
from qf_lib.common.enums.trade_field import TradeField


class TestScenariosGenerator(TestCase):

    def setUp(self):
        self.generator = ScenariosGenerator()

        self.num_of_scenarios = 100000
        self.scenarios_length = 7

    def test_make_scenarios(self):
        first_ret_value = 0.05
        second_ret_value = 0.1

        trade_rets = pd.Series([first_ret_value, second_ret_value], name=TradeField.Return)

        scenarios_df = self.generator.make_scenarios(trade_rets, self.scenarios_length, self.num_of_scenarios)

        expected_shape = (self.scenarios_length, self.num_of_scenarios)
        actual_shape = scenarios_df.shape
        self.assertAlmostEqual(expected_shape, actual_shape)

        values_count = scenarios_df.iloc[0, :].value_counts(normalize=True)

        first_return_freq = values_count[first_ret_value]
        second_return_freq = values_count[second_ret_value]

        expected_frequency = 0.5
        self.assertAlmostEqual(first_return_freq, expected_frequency, delta=0.01)
        self.assertAlmostEqual(second_return_freq, expected_frequency, delta=0.01)


if __name__ == '__main__':
    unittest.main()
