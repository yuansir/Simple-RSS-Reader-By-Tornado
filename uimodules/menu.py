# -*- coding: utf-8 -*-
from uimodules import UIModule

class MenuModule(UIModule):
    def render(self):
        category = [item['name'] for item in self.db.category.find().sort("name")]
        if u'Other' not in category:
            category.append('Other')

        list = dict()
        for c in category:
            list[c] = [r for r in self.db.rss.find({'category': c},) if c == r['category']]
        return self.render_string('menu.html', list=list)
