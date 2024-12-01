# Currency Converter Terminal CLI Application

## Table Of Contents

1. [Overview](#overview)
2. [Features and Functions](#features-and-functions)
3. [Set Up](#set-up)
4. [Application Help](<#application help>)
5. [References](#references)

## Overview

This terminal command-line interface (CLI) application is a Currency Converter that helps users to convert the currency or currencies of their choice.
This is an ideal application for users travelling overseas or sending money overseas as this app allows the user to convert the value of money using the live exchange rate or the actual FX (Foreign Exchange) rate they received when they exchanged money (as often the received rate is generally lower than the live rate due to fees and commissions).

## Features and Functions
- Convert currencies using the live FX rate
    - The app will take the user's selections of base currency to convert to selected foriegn currency using the live FX rate.
- Convert currencies using an actual FX rate
    - The user can input an FX rate and a value amount and the app will output the converted amount either to base currency or foreign currency based on the user's selection - this way the user can track how much they are spending in base currency. 
    (eg. when the user goes overseas and exchanges money, the rate may be worse than the market rate).
    - Similarly this function can be used when sending money overseas 
    (eg. you want to send the value of 100 in foreign currency but don't know how much that is in your base currency).
- Calculate the actual FX rate
    - The user can input the base currency value and the foreign currency value and the app will calculate the FX rate.
- Save live FX rate conversions to a file
    - The user can choose to save the conversion for their own record.
- View conversion history
    - The user can view their saved conversions.

## System Requirements

System requirements are either macOS, Windows or Linux (with Python3 installed).
Any modern laptop or destop computer should suffice.

## Set Up

This application is run in terminal CLI and requires the latest python3 version installed.  
Please use the links under installation for step to install.

### Installation

1. [Python3](https://realpython.com/installing-python/)
2. [Terminal for Windows](https://medium.com/@bonguides25/how-to-install-and-update-windows-terminal-in-windows-10-11-b85361b1aa07#:~:text=The%20first%20and%20easiest%20way,minutes%20to%20download%20and%20install.)
3. [Terminal for Mac](https://medium.com/@latusikl/the-ultimate-setup-for-macos-terminal-7fd340f58366)
4. [Visual Studio Code](https://code.visualstudio.com/docs/setup/setup-overview)
5. The dependant packages are listed below and are installed through the terminal virtual environment.
    To enter into the virtual environment, follow these steps in terminal before installing the dependant packages:  
    i. input: ```python3 -m venv .venv```   
        - once the the program has run you will see a folder name .venv  
    ii. input: ```source .venv/bin/activate```  
        - this will activate to virtual environment. You can then run the pip install command for the corresponding packages per below.   
    iii. input: ```deactivate```  
        - this will exit out of the virtual environment  

### Dependencies and Licenses

The application is dependant on the following packages. Once you have entered into virtual environment (steps provided under Installation), run the pip install command per below to install the packages. 
List of required packages are under requirements.txt file.  

- colored==2.2.4 - this package is used to style the text in different colours
    - license: MIT License
    - copyright 2014 - 2023 Dimitris Zlatanidis
    - ```pip install colored```
- currency-codes==23.6.4 - this package provides a list of all currency codes
    - license: GNU General Public License v3.0
    - copywrite 2007 free sottware foundation
    - ```pip install currency-codes```
- tabulate==0.9.0 - this package is used to format the currency codes list
    - license: MIT License (MIT)
    - copywrite 2011 - 2020 Sergey Astanin
    - ```pip install tabulate```
- pytest==8.3.3 - this package is used to run test code
    - license: MIT License (MIT)
    - copywrite 2004 Holger krekel and others
    - ```pip install pytest```
- python-dotenv==1.0.1 - this package is used to to store sensitive data, for this app it is the API Key
    - license: BSD License (BSD-3-Clause)
    - copywrite 2014 Saurabh Kumar (python-dotenv), 2013 Ted Tieken (django-dotenv-rw), 2013 Jacob Kaplan-Moss (django-dotenv)
    - ```pip install python-dotenv```
- http://api.exchangeratesapi.io/v1/convert - license: Master Software as a Service Subscription Agreement (SaaS) 
    - the API key is used to extract live FX rates
    - the exchangerates API Key code is stored in .env for privacy protection

### Ethical Impact of the Licenses

#### MIT License 

Grants users the freedom to use, modify and distribute the software with no legal barriers for personal and commerical purposes.

#### GNU General Public License v3.0

Grants users the freedom and right to use. Any modified work must be licensed under General Public License and shared to ensure the software remains free to use. 

#### BSD License (BSD-3-Clause)

Grants users the freedom to use, modify and distribute the software with minimal restrictions on redistribution.

## Application Help

Open the terminal and run the application.  
(Ensure the set-up and installation steps have been completed).  

- Check python version by inputing in command line.  
```python --version``` or ```python3 --version```  
- To run the application, depending on your system and set-up, you may use <u>python</u> or <u>python3</u> and the file name. In this case main.py  
```python main.py``` or ```python3 main.py```  

You will see a welcome message and a list of selections below.

Simply enter the number corresponding to your selection.  

- ```Enter 1 to convert currencies using live FX rate.```
    - ```Please enter the amount you wish to convert:``` *This needs to be a numerical value.*
    - ```Please enter the currency code you wish to convert from:``` *The currency code is a 3 letter code representing the currency of choice (if unsure you can view the currency code by entering 4 in the main menu).*
    - ```Please enter the currency code you wish to convert to:``` *The currency code is a 3 letter code representing the currency of choice (if unsure you can view the currency code by entering 4 in the main menu).*
    - ```Enter a short description to save a history or enter to exit:``` *If you want to save a history of this conversion, enter a short description otherwise enter with no description will not save.*
    
- ```Enter 2 to convert currencies using your personalised FX rate.```
    - ```Please enter the FX rate you received during your exchange:``` *This is the FX rate given when you the the exchange.*
    - ```Please enter the value you wish to convert:``` *This is the monetary value.*
    - ```Do you want this value "x" converted to your base currency? Enter Y or N:``` *to assist with the calculation, enter Y if this is to be converted back to your base currency, (if the value you had input in the above line is the foreign value) otherwise enter N.*

- ```Enter 3 to calculate the FX rate.```
    - ```Please enter the from value to calculate the FX rate:``` *This is the base monetary value.*
    - ```Please enter the to value to calculate the FX rate:``` *This is the foreign monetary value.*

- ```Enter 4 to view the currency code list.```
    - *By entering 4, the Currency Code table will automatically populate.*

- ```Enter 5 to view conversion history.```
    - *By entering 5, the conversion history list will appear if available.*

- ```Enter 6 to exit.```
    - *By entering 6, you will exit the application and a farewell message will appear.*

## References

- Astanin, S. (2022). tabulate: Pretty-print tabular data. [online] PyPI. Available at: https://pypi.org/project/tabulate/.

- bonguides.com (2024). How to Install and Update Windows Terminal in Windows 10/11. [online] Medium. Available at: https://medium.com/@bonguides25/how-to-install-and-update-windows-terminal-in-windows-10-11-b85361b1aa07#:~:text=The%20first%20and%20easiest%20way [Accessed 23 Sep. 2024].

- code.visualstudio.com. (2024). Setting up Visual Studio Code. [online] Available at: https://code.visualstudio.com/docs/setup/setup-overview.

- docs.pytest.org. (n.d.). How to monkeypatch/mock modules and environments - pytest documentation. [online] Available at: https://docs.pytest.org/en/stable/how-to/monkeypatch.html.

- docs.python.org. (n.d.). 9. Classes — Python 3.8.4rc1 documentation. [online] Available at: https://docs.python.org/3/tutorial/classes.html.

- dslackw (2023). colored: Simple library for color and formatting to terminal. [online] PyPI. Available at: https://pypi.org/project/colored/.

- Holger, H., Oliveira, B., Pfannschmidt, R., Bruynooghe, F., Laugher, B. and Bruhin, F. (2024). pytest: pytest: simple powerful testing with Python. [online] PyPI. Available at: https://pypi.org/project/pytest/.

- krekel, holger and Team, P. (n.d.). How to monkeypatch/mock modules and environments - pytest documentation. [online] docs.pytest.org. Available at: https://docs.pytest.org/en/stable/how-to/monkeypatch.html.

- Kuchumov, A. (2023). currency-codes. [online] PyPI. Available at: https://pypi.org/project/currency-codes/ [Accessed 23 Sep. 2024].

- Kumar, S. (2024). python-dotenv: Add .env support to your django/flask apps in development and deployments. [online] PyPI. Available at: https://pypi.org/project/python-dotenv/.

- Łukasz Latusik (2023). The Ultimate Setup for macOS Terminal | Medium. [online] Medium. Available at: https://medium.com/@latusikl/the-ultimate-setup-for-macos-terminal-7fd340f58366 [Accessed 23 Sep. 2024].

- Mozilla (2023). HTTP Response Status Codes. [online] MDN Web Docs. Available at: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status.

- python.org (2020). 8. Errors and Exceptions — Python 3.8.1 documentation. [online] Python.org. Available at: https://docs.python.org/3/tutorial/errors.html.

- Stack Overflow. (2024a). Module not found running on command line. [online] Available at: https://stackoverflow.com/questions/55102788/module-not-found-running-on-command-line [Accessed 24 Sep. 2024].

- Stack Overflow. (2024b). python exception message capturing. [online] Available at: https://stackoverflow.com/questions/4690600/python-exception-message-capturing [Accessed 24 Sep. 2024].

- TrickSumo (2023). Setting Up OpenAI API Key in Visual Studio Using Python and Dotenv. [online] YouTube. Available at: https://www.youtube.com/watch?v=x5rscbij8SA [Accessed 25 Sep. 2024].

‌



