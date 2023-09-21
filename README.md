# creepin-crud

Base connectivity and CRUD for SQLAlchemy ORMs


## Development

Install dependencies:

```
pip install -r requirements-dev.txt
```

If using pyenv and a virtualenv, set the local pyenvs. E.g.:

```
pyenv local 3.8.10 3.9.2
```

Run tests with coverage:

```
tox
```


## Connectivity configuration

Database URI formats are documented in the [SQLAlchemy Engine configuration docs](
https://docs.sqlalchemy.org/en/14/core/engines.html)
