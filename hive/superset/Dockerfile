FROM apache/superset

WORKDIR /app
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    SUPERSET_ENV=production \
    FLASK_APP="superset.app:create_app()" \
    PYTHONPATH="/app/pythonpath" \
    SUPERSET_HOME="/app/superset_home" \
    SUPERSET_PORT=8088
HEALTHCHECK CMD curl -f "http://localhost:$SUPERSET_PORT/health"

EXPOSE ${SUPERSET_PORT}


# Switching to root to install the required packages
USER root
# Example: installing the MySQL driver to connect to the metadata database
# if you prefer Postgres, you may want to use `psycopg2-binary` instead
RUN pip install mysqlclient
RUN pip install sqlalchemy==1.4.23 
RUN pip install google
# Switching back to using the `superset` user
# We add the superset_config.py file to the container
COPY superset_config.py ${PYTHONPATH}/
# We tell Superset where to find it
ENV SUPERSET_CONFIG_PATH ${PYTHONPATH}/superset_config.py

# We switch back to the `superset` user
USER superset
