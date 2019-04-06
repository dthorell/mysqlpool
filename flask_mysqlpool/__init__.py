"""
    flask_mysqlpool
    ~~~~~~~~~~~~~~~~

    :copyright: (c) 2019 by Daniel Thorell.
    :license: BSD, see LICENSE for more details.
"""

import mysql.connector.pooling
from flask import current_app, _app_ctx_stack

__version__ = '1.0.2'


class MySQLPool(object):
    def __init__(self, app=None):
        self.cnx = None
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('MYSQL_HOST', 'localhost')
        app.config.setdefault('MYSQL_PORT', 3306)
        app.config.setdefault('MYSQL_USER', 'root')
        app.config.setdefault('MYSQL_PASS', '')
        app.config.setdefault('MYSQL_DB', 'tmp')
        app.config.setdefault('POOL_NAME', 'mysql_pool')
        app.config.setdefault('POOL_SIZE', 5)
        app.config.setdefault('AUTOCOMMIT', True)

    def connect(self):
        connection = {
            'pool_name': current_app.config['POOL_NAME'],
            'pool_size': current_app.config['POOL_SIZE'],
            'autocommit': current_app.config['AUTOCOMMIT'],
            'host': current_app.config['MYSQL_HOST'],
            'port': current_app.config['MYSQL_PORT'],
            'user': current_app.config['MYSQL_USER'],
            'password': current_app.config['MYSQL_PASS'],
            'database': current_app.config['MYSQL_DB'],
        }
        self.cnx = mysql.connector.pooling.MySQLConnectionPool(**connection)
        return self.cnx

    @property
    def connection(self):
        ctx = _app_ctx_stack
        if not hasattr(ctx, 'mysqlpool'):
            ctx.mysqlpool = self.connect()
        return ctx.mysqlpool
