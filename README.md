# MagicLinkGenerator
An authentication library made for you to take control of your own authentication.

Owning a domain and an email can have several benefits, you don't have to use those random generated (random subdomain).something.(Whatever fancy TLD they now these days.)
It also has one more benefit that we are going to make use of in this library.


### SMTP server

A smtp server manages the outgoing mails and every Email provider must have it. It works on two ports SSL and non SSL  (Real ports can vary eg. 465 and 587).
When we go to our all fancy, customized and tagged dashboards which we never use properly, sends request for to send a mail.

### Tired of using third party auth providers.

Customiizing an authentication mail and when a user logs in is a satisfactory feeling, whereas using external libraries is a cumbersome process setup their SDK's send them analytics data even
after unchecking the send analytucs reports checkbox and not much customization to go with.


### Limits of this project
Ofcourse as your needs grow it might not be a good idea to manage such low level and of utmost Importance (Communication) servuce on your own but until then these are the limits
These may vary from providor to providor and depending on your mail plans

At the time of writing this with a normal HOSTINGER plan I had 3000/Mails/Day which is sufficient for a hobby project or even a small business.


## Instructions

1) Need a Redis instance.
   > docker pull redis

2) Setup this project <br />
`git clone git@github.com/ashweenmankash/magiclinkgenerator.git` <br />
` python -m venv env ` <br />
` source ./env/bin/activate ` <br />
` pip install -r requirements.txt ` <br />

3) Setup your .env files. <br />

`
  BROKER=redis://localhost:6379   <br />
  SECRET= a secret that is shared between you and your service <br />
  SMTP_SERVER=smtp.hostinger.com <br />
  SMTP_PORT=465 <br />
  MAIL_ADDRESS= your email address <br />
  MAIL_PASSWORD= your email's password <br />
  SERVICE_NAME= Your business name  <br />
`
4) Run!<br />
` python -m app `  <br />

## You can deploy this app directly on Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/Coitf7?referralCode=7TbvLJ)
