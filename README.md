# django-webscrapping

## Setup for Heroku Deployment

1. Create app in heroku

2. Add config var
   DISABLE_COLLECTSTATIC = 1

3. Touch requirements.txt and put details (tested empty is fine)

4. Touch runtime.txt and put details (tested without it is fine)

5. Touch Procfile and put details (make sure it is web: gunicorn appname.wsgi)

6. pipenv install gunicorn whitenoise

7. go to settings.py
   add your app url and localhost or allow all (_) to allowed hosts
   ALLOWED_HOSTS = ['django-webscrapping.herokuapp.com', '127.0.0.1']
   or
   ALLOWED_HOSTS = ['_']

   add this to middleware
   MIDDLEWARE = [ 'whitenoise.middleware.WhiteNoiseMiddleware']

8. import os

9. add these lines

   ```
   # Static files (CSS, JavaScript, Images)
   # https://docs.djangoproject.com/en/3.2/howto/static-files/

   BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATIC_URL = '/static/'

   # Extra places for collectstatic to find static files.
   STATICFILES_DIRS = (
       os.path.join(BASE_DIR, 'static'),
   )
   ```

More details please refer to https://devcenter.heroku.com/articles/django-app-configuration
https://devcenter.heroku.com/articles/django-assets

or google-fu
