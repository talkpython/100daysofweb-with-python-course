# Days 61 - 64 Database migrations with Alembic

Now you have seen the videos from this chapter, you're ready to evolve your database schema using Alembic. In this your-turn, you'll jump back to the original app we built when introducing SQLAlchemy, our Hovershare scooter sharing app.

## Day 1-2: Watch the video lessons

The first half of this 4-day block is to watch the videos. Feel free to play around with the sample code and other projects while going through the videos.

## Day 3: Install and configure alembic

Much of the code you will work with in this your-turn will have already been written and you have seen before. After all, migrations are about going from an existing db schema to another.

We will start with a copy of the hovershare app. You'll find it in a folder next to this `readme.md` in `hovershare`.

First thing is to get this app running. Here are the quick steps for that.

1. Open a terminal / command prompt in that folder. **Make SURE** that your working directory is the `hovershare_project` folder. This will matter for subsequent commands.
2. Create a virtual environment and activate it
3. [Optional] Upgrade pip and setup tools: `pip install -U pip setuptools`
4. Install the requirements: `pip install -r hovershare/requirements.txt`
5. Run the program (to verify this all worked). You should see something like:

```
(venv) $ python program.py

Enter a command, [r]ent, [a]vailable, [l]ocate, [h]istory, e[X]it: h
********* Your rental history ********* 
 * 2018-12-08 Hover-1 1st edition
 * 2018-12-07 Hover-1 1st edition
 * 2018-12-07 Hover-1 Sport 2nd edition
 * 2018-10-23 Hover-1 Sport 2nd edition
 * 2018-09-11 Hover-1 Sport 3nd edition
```

Now that you have the project all setup and running. Configure it in your favorite editor and make sure it still works.

Look through the code, especially notice the SQLAlchemy base class and the various SQLAlchemy model classes in `hovershare.data.models`.

## Day 4: Install alembic and add two migrations

With everything tee'd up, let's dig into alembic. You need to begin by **getting alembic by adding it to your `requirements.txt` file** and rerunning the install command.

```
(venv) $ pip install -r hovershare/requirements.txt
```

The you will "install" alembic for your project by running the command:

```
(venv) $ alembic init alembic
``` 

Look over your new files and folders alembic created to see what you have to work with.

Your project structure should look like this (directories only shown):

```
hovershare_project
│
├── alembic
│   └── versions
└── hovershare
    ├── data
    │   └── models
    ├── db
    ├── infrastructure
    └── services
```

To have alembic automatically detect migrations, you'll need to do two things.

1. Register the SQLAlchemy db connection string in `alembic.ini >  sqlalchemy.url` 
2. Import all the models and set the `target_metadata = SqlAlchemyBase.metadata`.

This is **harder** than it sounds. When we did this in the videos from our Pyramid web app, all we had to do was:

```
from billtracker.data.models import *
from billtracker.data.modelbase import SqlAlchemyBase
```

However, this worked because `billtracker` is a package (that's how Pyramid rolls). But this hovershare app is just a bunch of loose files that work together as modules. So it won't work out of the box here.

The fix is add the `data` folder manually to the PYTHON_PATH used by the import feature of Python. If you have the structure shown above (you should if you are following along), then your `env.py` file should have these elements in it:

```python
# alembic/env.py
import os

# Add the data folder to the path
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hovershare'))
print("Adding " + folder + " to python path for Alembic.")
sys.path.insert(0, folder)

# noinspection PyUnresolvedReferences
import data.__all_models
# noinspection PyUnresolvedReferences
from data.sqlalchemybase import SqlAlchemyBase

# ...

target_metadata = SqlAlchemyBase.metadata
```

Test that things are working by simply asking Alembic for the current status of the DB:

```
(venv) $ alembic current
```

That should run without crashing. :)

Now you'll make a change to your SQLAlchemy model, see it fail to run, then fix the error by migrating the DB schema with alembic.

Add a column to `Location`. This can really be whatever you want. If you want an example, we could add a postal code column which is a string.

Try running your app again. It should fail:

```
sqlalchemy.exc.OperationalError: no such column: locations.postal_code
```

Time to migrate the DB. Create a revision with the following command (adjusting the comment of course).

```
(venv) $ alembic revision --autogenerate -m "add postal column"
```

Then apply it to our DB

```
(venv) $ alembic upgrade head
```

You should see a message about adding the column and a new file in `alembic/versions`. Try the app once more. It should be migrated and running.

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfWeb**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofweb-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofweb-with-python-course/pulls).*


