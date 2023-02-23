from . import credential

ENGINE_PATH_WIN_AUTH = (
    DIALECT
    + "+"
    + SQL_DRIVER
    + "://"
    + DB_USERNAME
    + ":"
    + DB_PASSWORD
    + "@"
    + HOST
    + ":"
    + str(PORT)
    + "/?service_name="
    + SERVICE
)
