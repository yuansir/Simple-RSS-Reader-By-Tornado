# -*- coding: utf-8 -*-
from handlers import RequestHandler
from stripogram import html2text


class CategoryAddHandler(RequestHandler):
    def get(self):
        self.render('category/add.html')

    def post(self):
        category = html2text(self.get_argument('category', ''))
        if len(category) == 0:
            return self.response_json(0, 'Category Name Required')

        if self.db.category.find_one({'name': category}):
            return self.response_json(0, 'Category Exists')

        if self.db.category.insert({'name': category}):
            return self.response_json(1, 'Success')

        return self.response_json(0, 'Failed')


class CategoryDelHandler(RequestHandler):
    def post(self):
        category = html2text(self.get_argument('data_name', ''))
        result = self.db.category.remove({'name': category}, safe=True)
        if result['n'] == 0:
            return self.response_json(0, 'Delete Fail')

        self.db.rss.update({'category': category}, {'$set': {'category': 'Other'}})
        return self.response_json(1, 'Success')


class CategoryEditHandler(RequestHandler):
    def get(self,name):
        result = self.db.category.find_one({'name':name})
        if result == None:
            self._reason = 'No category'
            self.write_error(404)
        else:
            self.render('category/edit.html',name=result['name'])

    def post(self,name):
        category = self.get_argument('category','')
        if len(category) == 0:
            return self.response_json(0, 'Category Name Required')

        result = self.db.category.update({'name':name},{"$set":{"name":category}},safe=True)
        if result['n'] == 0:
            return self.response_json(0,'Update Fail')
        self.db.rss.update({"category":name},{"$set":{"category":category}})
        return self.response_json(1,'Success')
