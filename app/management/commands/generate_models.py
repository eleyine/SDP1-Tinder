from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from random import randint

from loremipsum import get_sentence, get_paragraph

class Command(BaseCommand):
    pass