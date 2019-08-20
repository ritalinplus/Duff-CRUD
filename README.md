# Rindus-CRUD
Basic credit card CRUD


## Create django project
sudo docker-compose run web django-admin startproject rinduscrud

## Change user
sudo chown -R $USER:$USER .

## Connect DB

In composeexample/settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

