# SQLAlchemy Workshop

## Local Development

To start working locally, you need to set up a database. You can easily do this in a Docker container using
the `docker-compose-local.yaml` file. To run it, execute the following command:

```shell
make docker-up
```

### Database GUI

In the `docker-compose-local.yaml` you also can notice that there's a service for pgAdmin. You can easily connect to it
locally on port `8888` and login with the credentials that are in that file as well.

Next, you need to register a connection to the database running in a separate Docker container. The database runs
on `localhost:5432`, but since it's in a Docker container, and you're trying to connect to it from pgAdmin, which also
runs in a Docker container, use the name of the service (`db` in this case) instead of `localhost`. Username, password,
as well as the database name, can be found in the `docker-compose-local.yaml` file.

### Work with CLI

To use the `dbm` CLI locally, simply install the package with `poetry`:

```shell
poetry install
```
