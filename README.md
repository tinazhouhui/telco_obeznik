# Telco Obězník

[![Codeac.io](https://static.codeac.io/badges/2-259418893.svg "Codeac.io")](https://app.codeac.io/github/tinazhouhui/telco_obeznik)

Pet project. Website that collects relevant information regarding the world of telecommunication.

## Reguirements
- Python3
- Valid CSV

## Run
```bash
python3 generate.py
```

## Unit testing

Simply run the command in bash in the root directory of your project:

```bash
python3 -m unittest tests/*
```

## Coverage report

run command to see the % of code covered by tests:
'''bash
 coverage run --omit=tests/* -m pytest tests/* && coverage report -m
'''
