import os
from superset.config import *
from sqlalchemy import *


SECRET_KEY = '1dBL8QOCromAwD0nEZijWL7vvgGJHm0WPNxpUlJFGQA6fSQaG4dhj5sPvCZ7KX'

def get_env_variable(var_name, default=None):
    """Get the environment variable or raise exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = 'The environment variable {} was missing, abort...' \
                .format(var_name)
            raise EnvironmentError(error_msg)

invocation_type = get_env_variable('INVOCATION_TYPE')
if invocation_type == 'COMPOSE':
    MYSQL_USER = get_env_variable('MYSQL_USER')
    MYSQL_PASS = get_env_variable('MYSQL_PASS')
    MYSQL_HOST = get_env_variable('MYSQL_HOST')
    MYSQL_PORT = get_env_variable('MYSQL_PORT')
    MYSQL_DATABASE = get_env_variable('MYSQL_DB')

    # The SQLAlchemy connection string.
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER,
                                                          MYSQL_PASS,
                                                          MYSQL_HOST,
                                                          MYSQL_PORT,
                                                          MYSQL_DATABASE)
elif invocation_type == 'RUN':
    SQLALCHEMY_DATABASE_URI = get_env_variable('DB_URL')
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DATA_DIR, 'superset.db')


ENABLE_PROXY_FIX=True
CELERY_CONFIG = CeleryConfig
create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)