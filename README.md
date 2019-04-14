 <img height="150" width="150" src="https://github.com/krzeelzb/ERP-system/blob/master/emka_trans/static/img/logo_text.png" alt="EMKA-trans logo"/> 


EMKA-trans is a web application designed to be used by transportation companies.

The functionalities include:

*Company owner:
  Mapping the route,
  Manual route calculation,
  Defining routes transport,
  Automatic travel determination,
  Order monitoring,
  Checking system data,
  Sending confirmation to the customer's email address about the order,
  Valuation of the order,
  Description of products, their quantity, data collection

*Customer of the company:
  Registration, Log in,
  Profile management,
  Orders management,
  The history of orders,
  Current orders ,
  Expected delivery date,
  Calculating the price of the order,
  Date of payment,

*Company supplier:
  Registration,Log in,
  Profile management,
  Management of available products,
  API for uploading excel




Installation and set up:
```
$ mkdir emka
$ cd emka
$ python3 -m venv myvenv
$ source myvenv/bin/activate
(myvenv) ~$ python -m pip install --upgrade pip
(myvenv) ~$ git clone https://github.com/mmamica/ERP-system.git
(myvenv) ~$ cd ERP-system
(myvenv) ~$ pip install -r requirements2.txt
(myvenv) ~$ cd emka_trans
(myvenv) ~$ python manage.py makemigrations
(myvenv) ~$ python manage.py migrate
(myvenv) ~$ python manage.py runserver
```
