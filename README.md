# Telco Obězník

[![Codeac.io](https://static.codeac.io/badges/2-259418893.svg "Codeac.io")](https://app.codeac.io/github/tinazhouhui/telco_obeznik)

Pet project. Website that shows relevant information regarding the world of telecommunication in Czechia and around the world.

## Requirements
- Python3
- NodeJS 10+
- Valid CSV


## Installation
```
#!bash

pip3 install
npm install
```

## Run
```bash
python3 generate.py
npm run start
```

## Unit testing

Simply run the command in bash in the root directory of your project:

```bash
python3 -m unittest tests/**/*.py
```

## Coverage report

run command to see the % of code covered by tests:
```bash
coverage run --omit=tests/*,/home/*,/usr/* -m pytest tests/* && coverage report -m
```
