from flask import Flask


class App:
    __instance = None

    @staticmethod
    def get_app():
        if App.__instance is None:
            App()
        return App.__instance

    def __init__(self):
        if App.__instance is not None:
            pass
        else:
            App.__instance = Flask("iHello")
