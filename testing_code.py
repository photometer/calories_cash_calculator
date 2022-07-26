import calories_and_cash_calculator as ccc


if __name__ == "__main__":
    calories_calculator = ccc.CaloriesCalculator(limit=1800)
    cash_calculator = ccc.CashCalculator(limit=1000)

    # for calories calculator
    r1 = ccc.Record(amount=439, comment='very tasty cookie')
    r2 = ccc.Record(amount=30, comment='juice', date='26.08.2021')

    # for cash calculator
    r3 = ccc.Record(amount=150, comment='matcha latte')
    r4 = ccc.Record(amount=2000, comment='debt to sister', date='01.10.2021')

    # for calories calculator
    for record in r1, r2:
        calories_calculator.add_record(record)

    # for cash calculator
    for record in r1, r2:
        cash_calculator.add_record(record)

    print(calories_calculator.get_calories_remained())
    print(cash_calculator.get_today_cash_remained('rub'))