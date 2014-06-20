# -*- coding: utf-8 -*-
from handlers import RequestHandler
import feedparser
from bson import ObjectId


class RssAddHandler(RequestHandler):
    def get(self):
        category = [item['name'] for item in self.db.category.find()]
        'Other' in category and category.remove('Other')
        self.render('rss/add.html', category=category)

    def post(self):
        category = self.get_argument('category', 'Other')
        link = self.get_argument('link', '')
        if self.db.rss.find_one({'feed_link': link}):
            return self.response_json(0, 'RSS Url Exists')

        rss = feedparser.parse(link)
        if not rss.feed:
            return self.response_json('0', 'RSS Url Error')

        self.db.rss.insert(dict(
            category=category,
            title=rss.feed.title,
            link=rss.feed.link,
            feed_link=link,
        ))
        return self.response_json(1, 'Success', rss)


class RssListHandler(RequestHandler):
    def get(self):
        feed_link = self.get_argument('feed_link', '')
        rss = feedparser.parse(feed_link)
        if not rss.entries:
            return self.response_json(0, 'No Articles', rss.entries)
        return self.response_json(1, 'Success', rss.entries)


class RssDelHandler(RequestHandler):
    def post(self):
        id = self.get_argument('data_name', '')
        print id
        result = self.db.rss.remove({'_id': ObjectId(id)}, safe=True)
        if result['n'] == 0:
            return self.response_json(0, 'Delete Fail')
        return self.response_json(1, 'Success')


class RssEditHandler(RequestHandler):
    def get(self, id):
        result = self.db.rss.find_one({'_id': ObjectId(id)})
        if result == None:
            self._reason = 'No RSS'
            self.write_error(404)
        else:
            category = [item['name'] for item in self.db.category.find()]
            'Other' in category and category.remove('Other')
            self.render('rss/edit.html', rss=result, category=category)

    def post(self, id):
        result = self.db.rss.find_one({'_id': ObjectId(id)})
        if result == None:
            return self.response_json(0, 'No RSS')

        category = self.get_argument('category', 'Other')
        link = self.get_argument('link', '')

        if result['feed_link'] == link:  #只改分类
            result = self.db.rss.update({'_id': ObjectId(id)}, {"$set": {"category": category}}, safe=True)
        else:
            if self.db.rss.find_one({'feed_link': link, "_id": {"$ne": ObjectId(id)}}):
                return self.response_json(0, 'RSS Url Exists')

            rss = feedparser.parse(link)
            if not rss.feed:
                return self.response_json('0', 'RSS Url Error')

            update_data = dict(
                category=category,
                title=rss.feed.title,
                link=rss.feed.link,
                feed_link=link,
            )
            result = self.db.rss.update({'_id': ObjectId(id)}, {"$set": update_data}, safe=True)
        if result['n'] == 0:
            return self.response_json(0, 'Update Fail')
        return self.response_json(1, 'Success')



