import os
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nsgat.settings')

import django
django.setup()
from blog.models import Links, LinksCategory


def init_work():
    with open('links.json', 'r') as file:
        data_links = json.load(file)
        for cat in sorted(data_links.keys()):
            lnk_cat = add_cat(cat)
            for lnk in sorted(data_links[cat], key=lambda x: x['title']):
                print('\t', lnk['title'])
                lnk_add = add_page(title=lnk['title'], url=lnk['url'], description=lnk['description'], cat=lnk_cat)


def add_page(cat, title, url, description, is_published=True):
    p = Links.objects.get_or_create(
        title=title,
        url=url,
        description=description,
        category=cat,
        is_published=is_published
    )[0]
    return p


def add_cat(name):
    c = LinksCategory.objects.get_or_create(name=name)[0]
    return c


if __name__ == '__main__':
    self_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(self_path)
    init_work()
