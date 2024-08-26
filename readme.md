# LocalStack Playground

The LocalStack Playground is a Docker Compose setup that provisions LocalStack alongside optional databases (Postgres, Oracle, MySQL) in Docker containers. It creates a local environment for testing and deploying AWS cloud-based applications that access relational databases (RDBMS).

By default, the selected databases are initialized with the Chinook sample database. However, you can customize the initialization using environment variables to point to a folder containing your own scripts.

## devtools.sh

`devtools.sh` defines aliases for common operations involving the playground. To install the aliases, run:

```bash
source devtools.sh
```

You can incorporate 'devtools.sh' into your own dev process to allow further customizations if needed.  For example

```
source "$(dirname "$0")/../../../localstack_playground/devtools.sh"

alias dev_up="playground_postgres; ./install_secrets.py"
alias dev_down="playground_down"
alias dev_reset="playground_reset"
```

## Starting the Playground

To start the playground with LocalStack and all the databases, run:

```bash
playground_up
```

To start only LocalStack:

```bash
playground_localstack
```

To start individual databases:

```bash
playground_postgres
playground_oracle
playground_mysql
```

## Stopping the Playground

To stop all containers but retain the database volumes, run:

```bash
playground_down
```

## Resetting the Playground

Resetting the playground stops all containers and removes the database volumes. After a reset, databases will reinitialize on the next start.

```bash
playground_reset
```

## Accessing Playground Resources

Localstack services are usually available at the endpoint;

```
https://localhost.localstack.cloud:4566
```

Here are the connection parameters to access the playgrounds databases;

| Parameter | Postgres               | Oracle    | MySQL    |
|-----------|------------------------|-----------|----------|
| Database  | chinook_auto_increment | XEPDB1    | chinook  |
| Username  | chinook_user           | system    | root     |
| Password  | chinook_password       | system    | mysql    |
| Host      | postgres_db            | oracle_db | mysql_db |
| Port      | 5432                   | 1521      | 3306     |

> Host names apply only to network access within Localstack

## Configuration

By default, the playground initializes databases using the provided data set. You can override this by setting the following environment variables to point to a custom folder:

- `POSTGRES_INIT_DB`
- `ORACLE_INIT_DB`
- `MYSQL_INIT_DB`

For example, to use a custom folder for Postgres initialization:

```bash
POSTGRES_INIT_DB=./my_postgres_db playground_postgres
```

--- 

This version is more concise and structured, with consistent terminology and formatting.