"""Calories / cash calculator.

This module provides calories/cash statistics for today and last 7 days, 
allows to set a daily limit and check if it is reached (how much is left - 
if not).
"""
import datetime as dt

FORMAT = '%d.%m.%Y'


class Record:
    """Record object of input data for calculator.

    Attributes:
        amount: A numeric count of the spent cash/consumed calories in a day.
        comment: A string explanatory comment for spending/consuming.
        [date]: A string/datetime.date date for spending/consuming. Default 
                value: None.
    """

    def __init__(self, amount, comment, date = None):
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
        limit: A numeric daily limit for cash/calories.
    """

    def __init__(self, limit):
        """Inits Calculator class and list of input records."""
        self.limit = limit
        self.records = []
    
    def add_record(self, record):
        """Adds Record object to the list of records.
        
        Args:
            record: A Record object to add in the list of records

        No Returns.

        No Raises. 
        """
        self.records.append(record)

    def get_today_stats(self):
        """Returns calories/cash sum for today.
        
        No Args.
        
        Returns:
            A numeric count of calories/cash for today.
        
        No Raises.
        """
        day_amounts = 0
        for rec in self.records:
            if rec.date == dt.date.today():
                day_amounts += rec.amount
        return day_amounts

    def get_week_stats(self):
        """Returns calories/cash sum for last 7 days.
        
        No Args.
        
        Returns:
            A numeric count of calories/cash for last 7 days.
            
        No Raises.
        """
        week_amounts = 0
        # This comments are here due to the requirements of pytest.
        # List of timelta from days=0 to days=7 where day=7 is not included.
        week_delta = [dt.timedelta(days=day) for day in range(7)]
        for rec in self.records:
            if dt.date.today() - rec.date in week_delta:
                week_amounts += rec.amount    
        return week_amounts

            
class CaloriesCalculator(Calculator):
    """This class provides method for calculating remained calories for today 
    due to the daily limit and giving the text information about it.

    Attributes:
        limit: A numeric daily calories limit.
    """

    def get_calories_remained(self):
        """Checks if calories limit is reached and returns advice with
        remained calories for today (if limit is not reached).

        No Args.

        Returns:
            A string containing remained calories for today due to the daily
            limit (if not reached) and advice.

        No Raises.
        """
        remained = self.limit - super().get_today_stats()
        if remained > 0:
            return ('Сегодня можно съесть что-нибудь ещё, но '
                    'с общей калорийностью не более '
                    f'{remained} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    """This class provides method for calculating cash balance for today due 
    to the daily limit and giving the text information about it.

    Attributes:
        limit: A numeric daily cash limit.
    """

    USD_RATE = 60.
    EURO_RATE = 70.
    RUB_RATE = 1.
    CURRENCIES = {
                  'rub': ['руб', RUB_RATE],
                  'usd': ['USD', USD_RATE],
                  'eur': ['EUR', EURO_RATE],
                 }

    def get_today_cash_remained(self, currency):
        """Returns the amount of the cash balance from the limit.

        Args:
            currency: A string preference for output cash balance - 'rub' / 
                      'usd' / 'eur'.

        Returns:
            A string containing remained cash balance (if not 0) for today 
            due to the daily limit and advice.

        No Raises.
        """
        remained = ((self.limit - super().get_today_stats()) /
                    self.CURRENCIES[currency][1])
        selected_currency = self.CURRENCIES[currency][0]
        if remained > 0:
            return (f'На сегодня осталось {remained:.2f} '
                    f'{selected_currency}')
        elif remained < 0:
            return ('Денег нет, держись: твой долг - '
                    f'{abs(remained):.2f} {selected_currency}')
        else:
            return 'Денег нет, держись'          
