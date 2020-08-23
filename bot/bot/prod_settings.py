from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = 'sadbdabsdabjdb!!!cnsccds&&dasdasbcb!!&=5kh9sf!ou7k8doew&'

DEBUG = False

ALLOWED_HOSTS = [
    '89.223.126.211'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}