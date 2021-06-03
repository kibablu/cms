import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret-key"

    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT") or "projectoneblob"
    BLOB_STORAGE_KEY = (
        os.environ.get("BLOB_STORAGE_KEY")
        or "s/WknyVHJ+8+JKQ7CTbEJb55lAIamNH6PsX5nFTj0G8T9gE8HEQzrQ02/2rAEmath9kZEJaJAK8r33eYAL8gHg=="
    )
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER") or "images"

    SQL_SERVER = os.environ.get("SQL_SERVER") or "project-one.database.windows.net"
    SQL_DATABASE = os.environ.get("SQL_DATABASE") or "project-one-db"
    SQL_USER_NAME = os.environ.get("SQL_USER_NAME") or "student"
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD") or "aWkk*12Ghaykabcr"
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://"
        + SQL_USER_NAME
        + "@"
        + SQL_SERVER
        + ":"
        + SQL_PASSWORD
        + "@"
        + SQL_SERVER
        + ":1433/"
        + SQL_DATABASE
        + "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "Gdx.~cJNxt4ekdWq-j0Tv.yvrX2mzi40Y6"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "8b70bc9f-d0a9-4155-a7b1-c35055d196e9"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session