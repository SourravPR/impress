
# How to use this branch

This part of the seminar involves installing and getting started with django channels.

To get this running, simply run the  the following 

## Step 0 : Clone the Repository
git clone https://github.com/SourravPR/impress.git

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Run server

And start the server with 

`python manage.py runserver`

## Step 4 : Download and use ngrok
You need an HTTPS url for most webhooks for bots to work. For purely development purposes you can use ngrok. It gives a web-accessible HTTPS url that tunnels through to your localhost. Download ngrok (https://ngrok.com/) , got to a new tab on your terminal and start it with

`ngrok http 8000`

At this point, you will have to add the URLs to ALLOWED_HOSTS in chatbot_tutorial/settings.py.

## Step 5 : Talk to the BotFather and get and set your bot token
Start telegram, and search for the Botfather. Talk to the Botfather on Telegram and give the command /newbot to create a bot and follow the instructions to get a token.

Copy the token and paste in chatbot_tutorial/views.py

## Step 6 : Set your webhook by sending a post request to the Telegram API
type : `https://api.telegram.org/bot<token>/setWebhook?url=<ngrok url>` in a web browser and press enter
## Step 7 : Talk to the bot by starting with /start
