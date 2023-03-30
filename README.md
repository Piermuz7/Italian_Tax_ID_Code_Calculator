# Italian_Tax_ID_Code_Calculator

## What is the Italian Fiscal Code?
The Italian fiscal code, officially known in Italy as "Codice fiscale", is the tax code in Italy, similar to a Social Security Number (SSN) in the United States or the National Insurance Number issued in the United Kingdom. It is an alphanumeric code of 16 characters. The code serves to unambiguously identify individuals irrespective of citizenship or residency status. Designed by and for the Italian tax office, it is now used for several other purposes, e.g. uniquely identifying individuals in the health system, or natural persons who act as parties in private contracts. The code is issued by the Italian tax office, the Agenzia delle Entrate.
The algorithm for calculating the Italian tax code is available at the following link https://en.wikipedia.org/wiki/Italian_fiscal_code.
## What Is Italian_Tax_ID_Code_Calculator?
This is a simple Python application intended to provide a calculator of a person's Italian tax code. The objective of this calculator is to take as input a person's basic data such as surname, first name, date and place of birth and then output the Italian tax code.

## Prerequisites
- Python

## Usage
Open the terminal and perform the following steps:

First you have to install python libraries using pip:
```bash
 pip install -r requirements.txt
```
Then you can run the application:
```bash
 python3 tax_id_calculator.py SURNAME NAME YEAR_OF_BIRTH MONTH_OF_BIRTH DAY_OF_BIRTH PLACE_OF_BIRTH GENDER
```
If you have any doubts or problems while running the application, you can consult the options with the following command:
```bash
 python3 tax_id_calculator.py -h
```
or
```bash
 python3 tax_id_calculator.py --h
```
or
```bash
 python3 tax_id_calculator.py --help
```

## An Example with Mario Rossi

1. Input person data, in this case the personal data of Mario Rossi:
```bash
 python3 tax_id_calculator.py Rossi Mario 1985 12 10 "San Giuliano Terme" M
```
2. If the data is correct, the output will be a printout with all the input data and the calculated tax code as the last line. 
```
Surname: Rossi
Name: Mario
Birthday: 10/12/1985
Gender: M
Tax ID code: RSSMRA85T10A562S
```

## Future works
A web version of this application will be realised as future work.
Stay tuned ;)

## Contact

Piermichele Rosati - piermichele.rosati@gmail.com

Italian_Tax_ID_Code_Calculator: [https://github.com/Piermuz7/Italian_Tax_ID_Code_Calculator](https://github.com/Piermuz7/Italian_Tax_ID_Code_Calculator)
