# Calories / cash calculator

This module provides calories/cash stats for today and last 7 days, allows
to set a daily limit and check if it is reached (how much is left - if not).

## Calculator can:
- Save *new meal / spending money* record with ```add_record()``` method
- Count *how many calories are consumed / how much money is spent* today with
```get_today_stats()``` method
- Define *how many calories can be consumed* today with
```get_calories_remained()``` method
- Define *how much money can be spent today in RUB, USD or EUR* with
```get_today_cash_remained(currency)```
- Count *how many calories are consumed / how much money is spent* in last
7 days with ```get_week_stats()``` method
 
## Examples
- Required input data
    ```
    calories_calculator = CaloriesCalculator(limit=1800)
    cash_calculator = CashCalculator(limit=1000)
    ```
- Create records (amount and comment are required!)
    ```
    # for calories calculator
    r1 = Record(amount=439, comment='very tasty cookie')
    r2 = Record(amount=30, comment='juice', date='26.08.2021')
    
    # for cash calculator
    r3 = Record(amount=150, comment='matcha latte')
    r4 = Record(amount=2000, comment='debt to sister', date='01.10.2021')
    ```
- Save records
    ```
    # for calories calculator
    for record in r1, r2:
        calories_calculator.add_record(record)
    
    # for cash calculator
    for record in r1, r2:
        cash_calculator.add_record(record)
    ```
- Output results
    ```
    print(calories_calculator.get_calories_remained())
    print(cash_calculator.get_today_cash_remained('rub'))
    
    >>> Today you can eat something else but with a total calorie content of
    no more than 1361 kcal
    Left for today: 561.00 RUB
    ```

## More about output format
- The ```get_calories_remained()``` method return answers:
    - "Today you can eat something else, but with a total calorie content of
    no more than N kcal", if the ```limit``` is not reached,
    - "Stop eating!", if the ```limit``` is reached or exceeded,

- The ```get_today_cash_remained(currency)``` method must take ```currency```
as input: one of the strings 'rub', 'usd' or 'eur'. It returns a message about
the state of the daily balance in this currency, rounding the amount to 2
decimal places (to hundredths):
    - "Left for today: N RUB/USD/EUR", if the ```limit``` is not reached;
    - "No money, hold on!", if the ```limit``` is reached;
    - "No money, hold on! Your debt: N RUB/USD/EUR", if the limit is exceeded.

    > **NOTE:** Specify the exchange rate with the constants ```USD_RATE```
    and ```EURO_RATE``` directly in the body of the
    ```class CashCalculator```.

## Project usage and structure

- You can clone this repository with
```git clone https://github.com/photometer/calories_cash_calculator```
- In this project folder create and activate virtual environment
(recommendations for Windows):
 ```
 python -m venv venv
 . venv/scripts/activate
 ```
 - Install pytest with ```pip install pytest==5.3.2``` or this way:
 ```
 pip install -r requirements.txt
 ```
 - Run pytest with command ```pytest```
 - The main code is in *calories_and_cash_calculator.py* and testing code
 is presented in *testing_code.py*

#### Author: [Elizaveta Androsova](https://github.com/photometer) :sunglasses:
