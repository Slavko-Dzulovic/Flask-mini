from config.__init__ import Config


class Production(Config):
    ENV_TYPE = "Prod"

    DB_NAME = 'praksa_baza'
    DB_USER = 'slavko.dzulovic'
    DB_PASSWD = 'pitajpedju'
    DB_HOST = '127.0.0.1'
    DB_PORT = 5432