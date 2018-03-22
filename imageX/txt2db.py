# !/usr/bin/env python
# coding:utf-8
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imageX.settings")

import django
django.setup()

from search.models import Image

def main():

    f = open('images.txt')
    for line in f:
        title, tag = line.split('****')
        Image.objects.create(title=title, tag=tag, image='media/image_cat')
    f.close()


if __name__ == "__main__":
    main()
    print('Done!')