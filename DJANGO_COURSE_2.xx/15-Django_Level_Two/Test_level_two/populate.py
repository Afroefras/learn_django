import os
# Configure settings for project, need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Test_level_two.settings')

import django
django.setup()

from NewApp.models import User
from faker import Faker

fakegen = Faker(['it_IT', 'en_US', 'ja_JP'])

def populate(N=5):
    for entry in range(N):
        # Create Fake Data for entry
        fake_first, fake_last = fakegen.name().split()[:2]
        fake_email = fakegen.email()

        # Create new User Entry
        webpg = User.objects.get_or_create(first_name=fake_first, last_name=fake_last, email=fake_email)[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
