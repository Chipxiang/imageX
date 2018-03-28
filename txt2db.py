import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imageX.settings")

import django
django.setup()

from image.models import Category

def main():
    f = open('category.txt')
    for line in f:
        category = line
        Category.objects.create(text=category)
    f.close()

if __name__ == "__main__":
    main()
    print('Done!')