# Setup project with venv

In order to install the project dependencies you have to create a **virtual environment** also called **venv** in the
project folder

```bash
pip install virtualenv
```

```bash
virtualenv {path_of_the_project}/venv(for exemple /home/user/groupe1project/venv)
```

Now that you have your virtual environment you have to activate it:

**Mac OS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Now the venv is activate, you can install the dependencies by running in te project folder:

```bash
pip -r install requirements.txt
```

# Run the application

From the project folder with venv activated:

```bash
python manage.py runserver 8000
```

Then you can go to the [admin](localhost:8000/admin) with the following credentials:

| Username | Password |
|----------|:--------:|
| antoine  | EFPLn0yc |