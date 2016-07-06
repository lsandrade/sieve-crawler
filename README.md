# Webcrawler - Sieve
An webcrawler built in Python to Sieve's challange that visits the "epocacosmeticos.com.br" domain, demand for all products and stores them in a CSV file.

## Dependencies
```
unittest
BeautifulSoup
urllib
requests
concurrent.futures
```

Built with Python 3.5

Testing:
```
$ python testeunitario.py
```

Running:
```
$ python runme.py
```

The result will be in 'products.csv' file after running.
```
CSV's structure:
ref - product's code
name - product's name
price - product's price. It will be * if product is unavailable
availablity - product's availability. Yes or no.
description - product's description
url - product's url
```
