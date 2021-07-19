## cornershop-backend-test

### Running the development environment

* `make up`
* `dev up`

##### Rebuilding the base Docker image

* `make rebuild`

##### Resetting the local database

* `make reset`

### Hostnames for accessing the service directly

* Local: http://127.0.0.1:8000

### Using NoraApp

* With NoraApp, if you are the super user, you will be able to create, read, update and delete, menus and its options. Also it will be able to see list o menus and list of orders.
* To access like user: 
  - user: norapp
  - password: norapp.* 
* If you're not logged like user, you will not able to create/update/delete menus and its option, a basic cliente, just will be able
  to access to watch the menu, a make orders.
* In case a client gets the specific url to access to create/update/delete, it will be redirect to a login form.

### Considerations to create Menus
* When a menu is created, the field "menu date" requires a date equal or greater than today.

### Considerations to Order
* The menu will be able to order util 11 CLT

### Customize "Send slack"
* Go to your slack
* Settings and administration -> Manage apps
* Build
* Create an app
* Add "App Name"
* Development Slack Workspace -> choose the workspace
* Press "Create App"
* Press "Incoming Webhooks" -> Turn on
* Press "Add new Webhook to Workspace"
* Select a channel (where you want send your notifications) -> Press "Allow"
* Copy the Weebhoook URL and add to slack_message.py

### Test menuapp
* python manage.py test apps/menuapp/

### Test coverage
* python manage.py test coverage apps/menuapp/
* coverage report
