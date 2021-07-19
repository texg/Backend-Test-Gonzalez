import requests
import os
import sys
import arrow
from .models import Menu, Option
from backend_test.celery import app

#Send Slack Message Using Slack API

def send_slack_message(message):
    payload = '{"text": "%s"}' % message
    import pdb; pdb.set_trace()
    response = requests.post(
        'https://hooks.slack.com/services/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',
        data=payload
    )



@app.task()
def send_menu_today_slack():
    date_today = arrow.utcnow().to('America/Santiago').format('YYYY-MM-DD')
    menu = Menu.objects.filter(menu_date=date_today).first()

    if menu:
        menu_id = menu.id
        options = menu.options.all()

        if len(options) >= 1:
            options_array = (str(option) for option in options)
            menu_link = f'\n http://0.0.0.0:8000/menu/{menu_id}'
            message_menu = 'Menu \n' + '\n '.join(options_array) + menu_link
        else:
            message_menu = 'Not options for today'
    else:
        message_menu = 'Not menu for today'

    send_slack_message(message_menu)
