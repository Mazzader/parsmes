from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = '=rxfy!1&_$l$0a&(nwpl606zh1n3b!!&=5kh9sf!ou7k8doew&'

DEBUG = True

ALLOWED_HOSTS = [
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
