CROP based on Wagtail demo
=======================

## Starting the dev site (after initial set-up, see below).
This will start the pythin dev server and make the site available on `localhost:8111`
```
vagrant up
fab vagrant runserver
```


## Dumping live database to local

Use can use the `etc/load_db_template.sh` to create your own local `load_db.sh` script, just edit `DEVOPS_DIR` and `PROJECT_DIR` to point at you appropriate directories then run `etc/load_db.sh cms-crop`. Or you can use the commands below.

To dump the live databse and load into a vagrant dev site

* go to devops and use the nornal ansible commands. This will dump the database to devops/backup

* the from the cms-crop repo run `fab vagrant restore_db:DUMP_FILEN_NAME`


## Dropping and recreating local vagrant database

```
vagrant ssh
psql -Upostgres 

# Once in postgres
DROP DATABASE wagtaildemo;
\q

# Recreate it from command line
createdb -Upostgres wagtaildemo
```

## Deploy to cms-crop.apps.pointnineseven.com (Digital Ocean - 107.170.246.103)
cd into devops and run

```
ansible-playbook -i hosts.ini provisioning/playbook.yml  -l cms-crop.apps.pointnineseven.com --ask-vault-pass
```

## Copying user uploaded images

You can use rsync for this. 

```
# Copying from staging to local vagrant
rsync -avz apps.pointnineseven.com:/usr/local/apps/cms-crop/media /Users/wilblack/django-projects/cms-crop


# Copying from staging to production
# First copy to local machine
rsync -avz apps.pointnineseven.com:/usr/local/apps/cms-crop/media /Users/wilblack/django-projects/cms-crop

# Then copy to proudction site. (You may need to change file permissions)
rsync -avz /Users/wilblack/django-projects/cms-crop/media caribbean-mp.org:/usr/local/apps/cms-crop-live
```

## Data Catalogs

Data catalogs (Themes and layers) are pulled from crop.apps.pointnineseven.com
To trigger this send a GET to `/webhook/?token=a5680aa0-3473-11e4-8c21-0800200c9a66&action=update-catalog`
This will run the `update_data_topics` in the background using Celery.

You need to have the celery worker running. In vagrant you can start the Celery worker with

```
celery -A wagtaildemo  worker -l info
```

JSON Object (with themes controlled by MP)

```
themes : [  // Themes shouldbe shorted in alphabetical order by english name.
{
    id: 27,
    name : "Administrative & Regulatory",
    short_description: "A short description",
    description : "A long description",

    spanish_name : "Espanol name",
    spanish_short_description: "Espanol short description",
    spanish_description: "Espanol description",

    layers: [ // Layers should be sorted in alphabetical order by name.
        {
            id : 370,
            name : "200NM EZ and Maritime Boundaries",
            description : "This layer contains the US 200nm EEZ as...",
            map_link : "",
            kml_link : "",
            data_link : "",
            tiles_link : "",
            meta_link : ""
        }, {
            id : 371,
            name : "",
            description : "",
            map_link : "",
            kml_link : "",
            data_link : "",
            tiles_link : "",
            meta_link : ""
        }
    ]
},
]
```


# Wagtail Docs

[Wagtail](http://wagtail.io) is distributed as a Python package, to be incorporated into a Django project via the INSTALLED_APPS setting. To get you up and running quickly, we provide a demo site with all the configuration in place, including a set of example page types.

Setup (with Vagrant - recommended)
-----

We recommend running Wagtail in a virtual machine using Vagrant, as this ensures that the correct dependencies are in place regardless of how your host machine is set up.

### Dependencies
* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant 1.1+](http://www.vagrantup.com)

### Installation
Run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py createsuperuser
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8111/ - you can access the Wagtail admin interface at http://localhost:8111/admin/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.

### Developing Wagtail
The above setup is all you need for trying out the demo site and building Wagtail-powered sites. To develop Wagtail itself, you'll need a working copy of [the Wagtail codebase](https://github.com/torchbox/wagtail) alongside your demo site, shared with your VM so that it is picked up instead of the packaged copy of Wagtail. From the location where you cloned wagtaildemo:

    git clone https://github.com/torchbox/wagtail.git
    cd wagtaildemo
    cp Vagrantfile.local.example Vagrantfile.local
        (edit Vagrantfile.local to specify the path to the wagtail codebase, if required)
    cp wagtaildemo/settings/local.py.example wagtaildemo/settings/local.py
        (uncomment the lines from 'import sys' onward, and edit the rest of local.py as appropriate)
    
If your VM is currently running, you'll then need to run `vagrant halt` followed by `vagrant up` for the changes to take effect.

Setup (without Vagrant)
-----
Don't want to set up a whole VM to try out Wagtail? No problem.

### Dependencies
* [PostgreSQL](http://www.postgresql.org)
* [PIP](https://github.com/pypa/pip)

### Installation

With PostgreSQL running (and configured to allow you to connect as the 'postgres' user - if not, you'll need to adjust the `createdb` line and the database settings in wagtaildemo/settings/base.py accordingly), run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    pip install -r requirements/dev.txt
    createdb -Upostgres wagtaildemo
    ./manage.py syncdb
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py runserver


## Troubleshooting

### CSS files not updating.
Django comrpessor should autmoatically recompress css files on page load. If your CSS changes are not showing up, this may be becuase there duplicates of the css files in the /static/. To fix delete everything in /static/ and then refresh your browser. There should only be CACHE/css in there. 



### Wagtail versions

Stable version on cms-crop - -e git://github.com/torchbox/wagtail.git@ccad0d96ed7f87e2b8be290321ae981df893e7c9#egg=wagtail-dev


Old version on Wil's vagrant 
-e git://github.com/torchbox/wagtail.git@765657329e529f828e0bbf0185c162570301a539#egg=wagtail-master
