import requests
import os
import sys
import arrow
# base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_path)
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_test.settings")
# sys.path.append(base_path)
# os.chdir(base_path)

from .models import Menu, Option

#Send Slack Message Using Slack API

def send_slack_message(message):
    payload = '{"text": "%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
                                data=payload)

    print(response.text)


def menu_today_slack():
    date_today = arrow.utcnow().to('America/Santiago').format('YYYY-MM-DD')
    menu = Menu.objects.filter(menu_date=date_today)

    if len(menu) > 1:
        menu_item = menu[0]
        menu_id = menu_item.id
        options = Option.objects.filter(menu=menu_id)

        if len(options) > 1:
            options_array = (str(option) for option in options)
            menu_link = f'\n http://0.0.0.0:8000/menu/{menu_id}'
            message_menu = 'Menu \n' + '\n '.join(options_array) + menu_link
            send_slack_message(message_menu)
        else:
            message_menu = 'Not options for today'
            send_slack_message(message_menu)
    else:
        message_menu = 'Not menu for today'
        send_slack_message(message_menu)

menu_today_slack()


