import unittest

from cwiczenie_12 import CashMachine


class TestCashMachine(unittest.TestCase):

    def test_cash_machine_is_not_available_after_creation(self):
        cm = CashMachine()
        self.assertFalse(cm.is_available)

    def test_cash_machine_is_available_after_put_money(self):
        cm = CashMachine()
        cm.put_money([100])
        self.assertTrue(cm.is_available)

    def test_cash_machine_withdraw_money_simple_case(self):
        cm = CashMachine()
        cm.put_money([100])
        self.assertEqual(cm.withdraw_money(100), [100])

    def test_cash_machine_withdraw_money_simple_case_2(self):
        cm = CashMachine()
        cm.put_money([200])
        self.assertEqual([], cm.withdraw_money(100))


    def test_cash_machine_withdraw_money_withdraw_many_bills(self):
        cm = CashMachine()
        cm.put_money([200, 100, 50])
        self.assertEqual([100, 50], cm.withdraw_money(150))

    def test_cash_machine_withdraw_money_withdraw_many_bills_different_order(self):
        cm = CashMachine()
        cm.put_money([200, 50, 100])
        self.assertEqual([100, 50], cm.withdraw_money(150))
        self.assertEqual([], cm.withdraw_money(150))