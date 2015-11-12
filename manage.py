#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sdp1_tinder.settings")
    # see django_boilerplate/settings/__init__.py
    os.environ.setdefault("APP_ENV", "dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
