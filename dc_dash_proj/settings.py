
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6n1gin#hsb98piodlju^4-49xv*fal4kvhs1ar=@@wk@4be&wc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
"""
# FOO_IMP_TBD - When Debug = False --- we go to --- Non Existing page == http://localhost:8000/adminddd
# We get the Custom 404.html page --- cant rename the 404.html to custom_404.html

ALSO 

# FOO_IMP_TBD - When Debug = False --FOR Nginx Prod- we go to --- Non Existing page == http://digitalcognition.co.in/admin_approved_acxxxccvv
# We get the Custom 404.html page --- cant rename the 404.html to custom_404.html

"""

ALLOWED_HOSTS = ['*']


## https://support.google.com/a/answer/176600?hl=en
## Below -- CFE + Gyaan on Google Link Above 

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'infobot2016@gmail.com'# FOO_IMP_TBD --- Change TBD
EMAIL_HOST_PASSWORD = '' ## FOO_IMP_TBD --- Change TBD
EMAIL_PORT = 587 ## FOR TLS 
#EMAIL_PORT = 465   ## FOR SSL 
EMAIL_USE_TLS = True


"""
Starts -- #DJANGO REGISTRATION_REDUX SETTINGS
"""
## SOURCE == https://github.com/macropin/django-registration/blob/ae105ff615c1d1b5c27e2dbb90a1df2455b6d556/test_app/settings_test.py#L53

ADMINS = (
    ('admin1', 'dhankar.rohit@gmail.com'), ## This email will receive Intimation for ERRORS / 404 / 500 etc when running in Production
    ('admin2', 'dhankar.rohit@gmail.com'), ## This email will receive Intimation for ERRORS / 404 / 500 etc when running in Production
)

## SOURCE == https://github.com/macropin/django-registration/blob/ae105ff615c1d1b5c27e2dbb90a1df2455b6d556/test_app/settings_test.py#L53

REGISTRATION_ADMINS = (
    ('admin1', 'rohit.dhankar@strategic-leadership-llc-india.com'),
    ('admin2', 'rohit.dhankar@strategic-leadership-llc-india.com'),
)

##FOO_IMP_TBD===TESTING# http://localhost:8000/admin_approved_accounts/activate/888a2142ccede4e3f32cafc8ee6eb8286239c970/

##https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-AUTH_USER_MODEL
#AUTH_USER_MODEL = 
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = False ## FOO_IMP_TBD CHECK 
SITE_ID = 2
#LOGIN_REDIRECT_URL = '/pyfintrader/index/' #URL user will LAND upon after LOGIN # FOO_IMP_TBD --- Change OR Duplicate for DC
#datasets_listView
LOGIN_REDIRECT_URL = '/dc/datasets_listView/'

#ACCOUNT_LOGOUT_REDIRECT_URL = '/pyfintrader/index/' ## Can be given if we dont want to give Branding message on Accounts Logout 
## Above -- is hit from == http://localhost:8000/admin_approved_accounts/register
## This is as coded in FILE == views.py == /dc_info_venv/lib/python3.5/site-packages/registration/views.py

REGISTRATION_EMAIL_HTML = True
REGISTRATION_OPEN = True 
INCLUDE_AUTH_URLS = True ## FOO_IMP_TBD Not sure if REQD
INCLUDE_REGISTER_URL = True ## FOO_IMP_TBD-- YES REQD -See File == urls.py == /site-packages/registration/backends/admin_approval/urls.py
## SITE_ID == https://stackoverflow.com/a/11814271/4928635
## FOO_IMP_TBD -- REGISTRATION_USE_SITE_EMAIL ==>> ## https://django-registration-redux.readthedocs.io/en/latest/quickstart.html
## FOO_IMP_TBD -- REGISTRATION_SITE_USER_EMAIL
## REGISTRATION_DEFAULT_FROM_EMAIL
## https://django-registration-redux.readthedocs.io/en/latest/quickstart.html

"""
FOO_IMP_TBD MAIN --- ENDS -- #DJANGO REGISTRATION_REDUX SETTINGS
"""

## Internationalization --- site will be Translated in other langs --- Russian etc 
USE_I18N = False
## False as when its Not required -- we keep Django from Uploading extra Libs etc -- Optimized Code

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes', ##django.contrib.contenttypes
    'django.contrib.sessions',
    'django.contrib.messages',
    
    'django.contrib.sites', ## For -- django-registration-redux -- to be able to POINT towards CLIENTS SITE --- pyfintrader.com etc ...
    'registration', #https://django-registration-redux.readthedocs.io/en/latest/quickstart.html
    # registration --- up here as fixes == https://github.com/macropin/django-registration/issues/140#issuecomment-380304995
    'django.contrib.admin',
    'django.contrib.staticfiles',
    
    ## Own APPS Below 
    #'crispy_forms', # CRISPY FORM TAGS
    'micawber.contrib.mcdjango',
   
    # 'pyfintrader',
    # 'pricingintell',
    # 'patentspike',
    # 'digitalcognition', # Same as == 'dc_dash', #JIRA_ROHIT - will change laters
    'dc_dash',
    'churn_app',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dc_dash_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [os.path.join(BASE_DIR, 'custom_error_templates')],
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dc_dash_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcdbapr20', ### DEFAULT SCHEMA == "public"
        'USER': 'dcdbapr20user', ### NO CAPITAL LETTERS in USER NAME for Postgres
        'PASSWORD': 'passdcdbapr20',
        'HOST': 'localhost', ## IF NO == localhost --- then ERROR.
        'PORT': '', ## Can be Blank for LocalHost
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#
MEDIA_URL = '/media/'
#MEDIA_ROOT = '/var/www/nginx_django_static/media_served_by_nginx/'
MEDIA_ROOT = BASE_DIR
#
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/') # Nginx Config
#STATIC_ROOT = '/var/www/nginx_django_static'
print("    =From Settings.py==Nginx Config======STATIC_ROOT=====    ",STATIC_ROOT)
print("    =From Settings.py==Nginx Config======BASE_DIR========    ",BASE_DIR)
print("  "*10)
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_digitalcog"),]
## STATICFILES_DIRS --- is where the Collectstatic will gather Files from and Push them to STATIC_ROOT 
## Nginx will serve the Files from - STATIC_ROOT 
#




