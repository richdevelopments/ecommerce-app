{"filter":false,"title":"settings.py","tooltip":"/ecommerce/settings.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":0,"column":0},"end":{"row":120,"column":0},"action":"remove","lines":["\"\"\"","Django settings for ecommerce project.","","Generated by 'django-admin startproject' using Django 1.11.20.","","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = 'i@n1qrpcc44t6ygc_ae8=9f5z9oq-k34i1p&^6i5kmh7iz7!u_'","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = ['e3958214b6894e3da119117ea0d0de5c.vfs.cloud9.us-east-1.amazonaws.com']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'ecommerce.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","            ],","        },","    },","]","","WSGI_APPLICATION = 'ecommerce.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":124,"column":74},"action":"insert","lines":["\"\"\"","Django settings for ecommerce project.","Generated by 'django-admin startproject' using Django 1.11.15.","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = 'bi6@b(9cet7qbrq)@0k%^w*@9pu@k8telu#vqghlch@b@xks+4'","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME'), '127.0.0.1']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    'django_forms_bootstrap',","    'accounts',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'ecommerce.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [os.path.join(BASE_DIR, 'templates')],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","            ],","        },","    },","]","","WSGI_APPLICATION = 'ecommerce.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.CaseInsensitiveAuth'","]","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","","MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'"]}],[{"start":{"row":24,"column":17},"end":{"row":24,"column":46},"action":"remove","lines":["os.environ.get('C9_HOSTNAME')"],"id":3},{"start":{"row":24,"column":17},"end":{"row":24,"column":86},"action":"insert","lines":["'e3958214b6894e3da119117ea0d0de5c.vfs.cloud9.us-east-1.amazonaws.com'"]}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"remove","lines":["e"],"id":4},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"remove","lines":["u"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"remove","lines":["r"]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"remove","lines":["T"]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["F"],"id":5},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["a"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["l"]},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["s"]},{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"remove","lines":["e"],"id":6},{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"remove","lines":["s"]},{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"remove","lines":["l"]},{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"remove","lines":["a"]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"remove","lines":["F"]}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["T"],"id":7}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"remove","lines":["T"],"id":8},{"start":{"row":22,"column":8},"end":{"row":22,"column":12},"action":"insert","lines":["True"]}],[{"start":{"row":0,"column":0},"end":{"row":124,"column":74},"action":"remove","lines":["\"\"\"","Django settings for ecommerce project.","Generated by 'django-admin startproject' using Django 1.11.15.","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = 'bi6@b(9cet7qbrq)@0k%^w*@9pu@k8telu#vqghlch@b@xks+4'","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = ['e3958214b6894e3da119117ea0d0de5c.vfs.cloud9.us-east-1.amazonaws.com', '127.0.0.1']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    'django_forms_bootstrap',","    'accounts',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'ecommerce.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [os.path.join(BASE_DIR, 'templates')],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","            ],","        },","    },","]","","WSGI_APPLICATION = 'ecommerce.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.CaseInsensitiveAuth'","]","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","","MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'"],"id":9},{"start":{"row":0,"column":0},"end":{"row":125,"column":74},"action":"insert","lines":["\"\"\"","Django settings for ecommerce project.","Generated by 'django-admin startproject' using Django 1.11.15.","For more information on this file, see","https://docs.djangoproject.com/en/1.11/topics/settings/","For the full list of settings and their values, see","https://docs.djangoproject.com/en/1.11/ref/settings/","\"\"\"","","import os","","# Build paths inside the project like this: os.path.join(BASE_DIR, ...)","BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))","","","# Quick-start development settings - unsuitable for production","# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/","","# SECURITY WARNING: keep the secret key used in production secret!","SECRET_KEY = 'bi6@b(9cet7qbrq)@0k%^w*@9pu@k8telu#vqghlch@b@xks+4'","","# SECURITY WARNING: don't run with debug turned on in production!","DEBUG = True","","ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME'), '127.0.0.1']","","","# Application definition","","INSTALLED_APPS = [","    'django.contrib.admin',","    'django.contrib.auth',","    'django.contrib.contenttypes',","    'django.contrib.sessions',","    'django.contrib.messages',","    'django.contrib.staticfiles',","    'django_forms_bootstrap',","    'accounts',","    'products',","]","","MIDDLEWARE = [","    'django.middleware.security.SecurityMiddleware',","    'django.contrib.sessions.middleware.SessionMiddleware',","    'django.middleware.common.CommonMiddleware',","    'django.middleware.csrf.CsrfViewMiddleware',","    'django.contrib.auth.middleware.AuthenticationMiddleware',","    'django.contrib.messages.middleware.MessageMiddleware',","    'django.middleware.clickjacking.XFrameOptionsMiddleware',","]","","ROOT_URLCONF = 'ecommerce.urls'","","TEMPLATES = [","    {","        'BACKEND': 'django.template.backends.django.DjangoTemplates',","        'DIRS': [os.path.join(BASE_DIR, 'templates')],","        'APP_DIRS': True,","        'OPTIONS': {","            'context_processors': [","                'django.template.context_processors.debug',","                'django.template.context_processors.request',","                'django.contrib.auth.context_processors.auth',","                'django.contrib.messages.context_processors.messages',","            ],","        },","    },","]","","WSGI_APPLICATION = 'ecommerce.wsgi.application'","","","# Database","# https://docs.djangoproject.com/en/1.11/ref/settings/#databases","","DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}","","","# Password validation","# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators","","AUTH_PASSWORD_VALIDATORS = [","    {","        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',","    },","    {","        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',","    },","]","","AUTHENTICATION_BACKENDS = [","    'django.contrib.auth.backends.ModelBackend',","    'accounts.backends.CaseInsensitiveAuth'","]","","# Internationalization","# https://docs.djangoproject.com/en/1.11/topics/i18n/","","LANGUAGE_CODE = 'en-us'","","TIME_ZONE = 'UTC'","","USE_I18N = True","","USE_L10N = True","","USE_TZ = True","","","# Static files (CSS, JavaScript, Images)","# https://docs.djangoproject.com/en/1.11/howto/static-files/","","STATIC_URL = '/static/'","","MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'"]}],[{"start":{"row":24,"column":17},"end":{"row":24,"column":46},"action":"remove","lines":["os.environ.get('C9_HOSTNAME')"],"id":10},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["'"]},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":["'"]}],[{"start":{"row":24,"column":18},"end":{"row":24,"column":85},"action":"insert","lines":["e3958214b6894e3da119117ea0d0de5c.vfs.cloud9.us-east-1.amazonaws.com"],"id":11}],[{"start":{"row":63,"column":68},"end":{"row":63,"column":70},"action":"remove","lines":["',"],"id":14},{"start":{"row":63,"column":68},"end":{"row":64,"column":0},"action":"insert","lines":["",""]},{"start":{"row":64,"column":0},"end":{"row":64,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":64,"column":16},"end":{"row":64,"column":58},"action":"insert","lines":["'django.template.context_processors.media'"],"id":15}],[{"start":{"row":63,"column":68},"end":{"row":63,"column":69},"action":"insert","lines":[","],"id":16}],[{"start":{"row":63,"column":68},"end":{"row":63,"column":69},"action":"remove","lines":[","],"id":17}],[{"start":{"row":63,"column":68},"end":{"row":63,"column":69},"action":"insert","lines":["'"],"id":18}],[{"start":{"row":63,"column":69},"end":{"row":63,"column":70},"action":"insert","lines":[","],"id":19}],[{"start":{"row":64,"column":58},"end":{"row":64,"column":59},"action":"insert","lines":[","],"id":20}],[{"start":{"row":124,"column":23},"end":{"row":125,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":125,"column":0},"end":{"row":126,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":126,"column":0},"end":{"row":127,"column":21},"action":"insert","lines":["MEDIA_ROOT = os.path.join(BASE_DIR, 'media')","MEDIA_URL = '/media/'"],"id":22}]]},"ace":{"folds":[],"scrolltop":1821.5,"scrollleft":0,"selection":{"start":{"row":127,"column":21},"end":{"row":127,"column":21},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1564059823634,"hash":"e1a1849e66bc9a40e561dbe422f33935ec79da0b"}