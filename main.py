from framework.master import App
from urls.urls import routes
from framework.front_controllers import front_controllers

app = App(routes, front_controllers)