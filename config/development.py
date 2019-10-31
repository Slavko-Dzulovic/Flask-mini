from config.__init__ import Config


class Development(Config):
    ENV_TYPE = "Dev"

    DB_NAME = 'praksa_baza'
    DB_USER = 'slavko.dzulovic'
    DB_PASSWD = 'pitajpedju'
    DB_HOST = '127.0.0.1'
    DB_PORT = 5432
    # SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_DATABASE_URI = "postgres://skmcsgcshgphki:aa4f305ba603150397bc0594625510510feb2c6cfb389250a7438b680e50bc13@ec2-54-217-221-21.eu-west-1.compute.amazonaws.com:5432/dg5pgitsgt4qe"
