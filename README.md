# Wearhacks Montreal 2015 Website Source

# Installation

## Requirements

* `pip` - instructions [here](https://pip.pypa.io/en/latest/installing.html)
* `virtualenvwrapper` - instructions [here](https://virtualenvwrapper.readthedocs.org/en/latest/install.html)
* `npm` - instructions [here](https://docs.npmjs.com/getting-started/installing-node)

## Quick setup

```bash
$ git clone git@github.com:eleyine/Django-Boilerplate.git
$ cd Django-Boilerplate
$ chmod u+x setup.sh
# The next two steps are optional but strongly recommended
$ mkvirtualenv django-boilerplate
$ workon django-boilerplate
(django-boilerplate) $ ./setup.sh
```

**Note**: `setup.sh` will copy `example_private_settings.py` to `private.py`. If you are on your local machine in dev mode, there's no need to edit it. However, if you'd like to deploy, *please update `app/settings/private.py` with your sensitive and deployment-specific settings*.

**Manual install: what's in `setup.sh`?**

If you don't want to use `setup.sh`

```bash
$ mkvirtualenv django-boilerplate
$ workon django-boilerplate
(django-boilerplate) $ pip install -r requirements.txt
(django-boilerplate) $ bower install
(django-boilerplate) $ cp app/settings/example_private_settings.py app/settings/private.py
(django-boilerplate) $ python manage.py makemigrations
(django-boilerplate) $ python manage.py migrate
(django-boilerplate) $ python manage.py runserver
```

Now, open <http://127.0.0.1:8000/>.

## Usage

* To run on [localhost](http://127.0.0.1:8000/):

    ```bash
    $ workon wearhacks-website
    (wearhacks-website) $ python manage.py runserver
    ```

* By default, you will use the Django settings defined in `django_boilerplate/settings/dev.py`. 
* To use production settings defined in `django_boilerplate/settings/prod.py`:

    ```bash
    (wearhacks-website) $ export APP_ENV=prod
    (wearhacks-website) $ python manage.py runserver
    ```

* You can edit `django_boilerplate/settings/private.py` to enter sensitive and user-specific settings. All settings in `private.py` will override those defined in `dev.py` and `prod.py`. See `django_boilerplate/settings/__init__.py` for more information.

## Deployment on Digital Ocean

I wrote a `fabric` script to automate installation on Digital Ocean droplets using the one-step Django installation. If you are deploying elsewhere, you can have an idea of the steps to take by inspecting `server_files/fabfile.py`. 

Here are the setup instructions if you choose to do it with Digital Ocean. 

* Create a Digital Ocean droplet with a Django installation image
* Ssh into your droplet to obtain the postgresql database password. It will be displayed in the welcome message. 
* Copy `django_boilerplate/settings/private.py` to `django_boilerplate/settings/server_private.py` and uncomment the postgresql settings. Edit in your postgresql password from the step above.

* Make sure you have fabric installed locally. If you ran `setup.sh`, you already have it.
* In `django_boilerplate/server_files/`, copy `fab_config_example.py` and rename it to `fab_config.py`. Edit in in your deployment host address.
* Then in `server_files`, run `fab all`
* If you'd like a list of fab commands, run `fab -l`