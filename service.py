import os
import time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imageX.settings")
import django
django.setup()
from account.models import Member


def main():
    while True:
        time.sleep(10)
        rows = Member.objects.all()
        for member in rows:
            member.upload_quota = 5
            member.save()
            print(member.upload_quota)

if __name__ == "__main__":
    main()
