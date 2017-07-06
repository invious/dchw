# This is an example local_settings.py file.
# This file should be copied into `local_settings.py`

AWS_ACCESS_KEY = ''
AWS_SECRET_KEY = ''

if not AWS_ACCESS_KEY or not AWS_SECRET_KEY:
    raise ValueError('AWS keys must be set in local_settings.py')
