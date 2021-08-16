import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Practice.settings')

import django
# Import settings
django.setup()

import random
from PracticeApp.models import Students_Practice
from faker import Faker
from datetime import datetime

fakegen = Faker(['en_US', 'ja_JP'])
topics = ['Search','Social','Marketplace','News','Games','Classical','Data Science']


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):
        # Create Fake Data for entry
        first_name, last_name = fakegen.name().split()[:2]
        birthday = fakegen.date_between()
        age = int((datetime.now().date() - birthday).days/365.2425)
        email = fakegen.email()
        fav_topic = random.choice(topics)

        # Create new Students_Practice Entry
        student = Students_Practice.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            age=age,
            email=email,
            fav_topic=fav_topic
        )[0]

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(77)
    print('Populating Complete')
