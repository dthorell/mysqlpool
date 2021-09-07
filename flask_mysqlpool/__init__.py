"""
    flask_mysqlpool
    ~~~~~~~~~~~~~~~~

    :copyright: (c) 2019 by Daniel Thorell.
    :license: MIT, see LICENSE for more details.
"""

import mysql.connector.pooling
from flask import current_app, _app_ctx_stack

__version__ = "1.0.5"


class MySQLPool(object):
    def __init__(self, app=None):
        self.cnx = None
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("MYSQL_HOST", "localhost")
        app.config.setdefault("MYSQL_PORT", 3306)
        app.config.setdefault("MYSQL_USER", "root")
        app.config.setdefault("MYSQL_PASS", "")
        app.config.setdefault("MYSQL_DB", "tmp")
        app.config.setdefault("MYSQL_POOL_NAME", "mysql_pool")
        app.config.setdefault("MYSQL_POOL_SIZE", 5)
        app.config.setdefault("MYSQL_AUTOCOMMIT", True)
        app.config.setdefault("MYSQL_CHARSET", 'utf8mb4')
        app.config.setdefault("MYSQL_COLLATION", 'utf8mb4_0900_ai_ci')
        app.config.setdefault("MYSQL_POOL_RESET_SESSION", False)


    def connect(self):
        connection = {
            "pool_name": current_app.config["MYSQL_POOL_NAME"],
            "pool_size": current_app.config["MYSQL_POOL_SIZE"],
            "autocommit": current_app.config["MYSQL_AUTOCOMMIT"],
            "host": current_app.config["MYSQL_HOST"],
            "port": current_app.config["MYSQL_PORT"],
            "user": current_app.config["MYSQL_USER"],
            "password": current_app.config["MYSQL_PASS"],
            "database": current_app.config["MYSQL_DB"],
            "charset": current_app.config["MYSQL_CHARSET"],
            "collation": current_app.config["MYSQL_COLLATION"],
            "pool_reset_session": current_app.config["MYSQL_POOL_RESET_SESSION"],
        }
        self.cnx = mysql.connector.pooling.MySQLConnectionPool(**connection)
        return self.cnx

    @property
    def connection(self):
        ctx = _app_ctx_stack
        if not hasattr(ctx, "mysqlpool"):
            ctx.mysqlpool = self.connect()
        return ctx.mysqlpool
