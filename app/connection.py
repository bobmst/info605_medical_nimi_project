# import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.sql import text

from . import credential

# TODO teporary testing code remove in production
from . import credential_test as credential

ENGINE_PATH_WIN_AUTH = (
    credential.DB_DIALECT
    + "+"
    + credential.DB_SQL_DRIVER
    + "://"
    + credential.DB_USERNAME
    + ":"
    + credential.DB_PASSWORD
    + "@"
    + credential.DB_HOST
    + ":"
    + str(credential.DB_PORT)
    + "/?service_name="
    + credential.DB_SERVICE
)


# import sqlalchemy and ssh libraries
import sqlalchemy
from sshtunnel import SSHTunnelForwarder


class SSH_DB:
    def __init__(self):
        # Create a SSH tunnel
        self.server = SSHTunnelForwarder(
            credential.SSH_HOST,
            ssh_username=credential.SSH_USERNAME,
            ssh_password=credential.SSH_PASSWORD,
            remote_bind_address=(
                credential.SSH_REMOTE_ADDRESS,
                credential.SSH_REMOTE_PORT,
            ),
            local_bind_address=("", credential.SSH_LOCAL_PORT),
        )

    def __enter__(self):
        self.server.start()
        # create an engine with connection string via SSH tunnel
        # self.engine = sqlalchemy.create_engine(db_credentials)

    def __exit__(self, exc_type, exc_value, traceback):
        self.server.stop()


class OracleConnection:
    def __init__(self):
        with SSH_DB() as server:
            self.engine = sqlalchemy.create_engine(ENGINE_PATH_WIN_AUTH)
        # self.ssh_port = ssh_port
        # engine = create_engine(ENGINE_PATH_WIN_AUTH)
        # return engine

    def __enter__(self):
        return self.engine.connect()

    def __exit__(self, exc_type, exc_value, traceback):
        self.engine.dispose()
