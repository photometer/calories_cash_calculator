"""Calories / cash calculator.

This module provides calories/cash stats for today and last 7 days, allows
to set a daily limit and check if it is reached (how much is left - if not).
"""
from __future__ import annotations
from typing import Optional
import datetime as dt

FORMAT: str = '%d.%m.%Y'


class Record:
    """Record object of input data for calculator.

    Attributes:
        amount: A count of the spent cash/consumed calories in a day.
        comment: An explanatory comment for spending/consuming.
        [date]: A date for spending/consuming. Default value: None.
    """

    amount: float
    comment: str
    date: dt.date

    def __init__(self, amount: float, comment: str,
                 date: Optional[str] = None) -> None:
        """Inits Record class and converts date to datetime.date format.

        If date is not mentioned it is assigned today date.
        """
        self.amount = amount
        self.comment = comment
        if date:
            self.date = dt.datetime.strptime(date, FORMAT).date()
        else:
            self.date = dt.date.today()


class Calculator:
    """This class contains info about the set daily limit for calories/cash.

    Attributes:
        limit: A daily limit for cash/calories.
    """

    WEEK_DELTA: dt.date = dt.date.today() - dt.timedelta(days=7)
    limit: float

    def __init__(self, limit: float) -> None:
        """Inits Calculator class and list of input records."""
        self.limit = limit
        self.records: list[Record] = []

    def add_record(self, record: Record) -> None:
        """Adds Record object to the list of records.

        Args:
            record: An object to add in the list of records.
        """
        self.records.append(record)

    def get_today_stats(self) -> float:
        """Returns calories/cash sum for today."""
        return sum(rec.amount for rec in self.records
                   if rec.date == dt.date.today())

    def get_week_stats(self) -> float:
        """Returns calories/cash sum for last 7 days."""
        return sum(rec.amount for rec in self.records
                   if dt.date.today() >= rec.date > self.WEEK_DELTA)

    def get_remained(self) -> float:
        '''Returns remained value due to the daily limit.'''
        return self.limit - self.get_today_stats()


class CaloriesCalculator(Calculator):
    """This class provides method for calculating remained calories for today
    due to the daily limit and giving the text information about it.

    Attributes:
        limit: A daily calories limit.
    """

    def get_calories_remained(self) -> str:
        """Checks if calories limit is reached and returns advice with
        remained calories for today (if limit is not reached).

        Returns:
            Remained calories for today due to the daily limit (if not
            reached) and advice.
        """
        remained = super().get_remained()
        if remained > 0:
            return ('Today you can eat something else but with a total '
                    f'calorie content of no more than {remained} kcal')
        return 'Stop eating!'


class CashCalculator(Calculator):
    """This class provides method for calculating cash balance for today due
    to the daily limit and giving the text information about it.

    Attributes:
        limit: A daily cash limit.
    """

    USD_RATE: float = 60.
    EURO_RATE: float = 70.
    RUB_RATE: float = 1.
    CURRENCIES: dict[str, tuple[str, float]] = {'rub': ('RUB', RUB_RATE),
                                                'usd': ('USD', USD_RATE),
                                                'eur': ('EUR', EURO_RATE), }

    def get_today_cash_remained(self, currency: str) -> str:
        """Returns the amount of the cash balance from the limit.

        Args:
            currency: A preference for output cash balance: 'rub'/'usd'/'eur'.

        Returns:
            A string containing remained cash balance (if not 0) for today
            due to the daily limit and advice.

        Raises:
            KeyError: If currency not found in the CURRENCIES dictionary.
        """
        remained = super().get_remained()
        if remained == 0:
            return 'No money, hold on!'
        if currency not in self.CURRENCIES:
            raise KeyError('No currency data')
        currency_name, currency_rate = self.CURRENCIES[currency]
        remained /= currency_rate
        if remained > 0:
            return (f'Left for today: {remained:.2f} {currency_name}')
        return ('No money, hold on! Your debt: '
                f'{abs(remained):.2f} {currency_name}')
