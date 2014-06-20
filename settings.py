# -*- coding: utf-8 -*-
import os

PORT = 8000

SETTING = dict(
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    static_path=os.path.join(os.path.dirname(__file__), 'static'),
    debug=True,
    autoreload=True,
    compiled_template_cache=False,
    cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    xsrf_cookies=True,
)

DB = {
    "mongo": {
        'host': '127.0.0.1',
        'port': 27017
    }
}