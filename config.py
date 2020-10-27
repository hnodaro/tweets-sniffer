import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '78w0o5tuuGex5Ktk8VvVDF9Pw3jv1MVE'