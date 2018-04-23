import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imageX.settings")

import django
django.setup()

from image.models import Category

def main():
    f = open('Category.txt')
    temp = f.read().splitlines()
    for i in temp:
        category = i
        print(i)
        Category.objects.create(text=category)
    f.close()

if __name__ == "__main__":
    main()
    print('Done!')