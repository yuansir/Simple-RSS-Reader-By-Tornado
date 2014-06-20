# -*- coding: utf-8 -*-
from handlers import index
from handlers import category
from handlers import rss

handler = [
    (r'/', index.IndexHandler),
    (r'/category-add', category.CategoryAddHandler),
    (r'/category-delete', category.CategoryDelHandler),
    (r'/category-edit/(.*)', category.CategoryEditHandler),
    (r'/rss-delete', rss.RssDelHandler),
    (r'/rss-add', rss.RssAddHandler),
    (r'/rss-list', rss.RssListHandler),
    (r'/rss-edit/(.*)', rss.RssEditHandler),
]
