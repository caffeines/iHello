from flask import Flask


class App:
    __instance = None

    @staticmethod
    def get_app():
        if App.__instance is None:
            App()
        return App.__instance

    def __init__(self):
        if not App.__instance:
            App.__instance = Flask("iHello")
