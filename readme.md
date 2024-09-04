# Localstack Playground

Localstack Playground is a Docker-based development environment designed for setting up and testing AWS services using LocalStack, with support for various RDBMS databases (Postgres, Oracle, MySQL). This environment facilitates local development and testing of cloud-based applications without the need to deploy to an actual AWS environment.

## Features

- **LocalStack Integration**: Simulates AWS cloud services locally, including S3, DynamoDB, and Lambda.
- **Database Support**: Includes containers for Postgres, Oracle, and MySQL, pre-configured with initialization scripts.
- **Flexible Setup**: Allows developers to start and stop individual services as needed.
- **Volume Management**: Automatically manages Docker volumes for database persistence.

## Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine.
- **Python 3.9+**: Required for running the provided management scripts.

## Installation

1. **Install Localstack Playground from PyPI**:
    ```bash
    pip install localstack-playground
    ```

2. **Set Up a Virtual Environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

## Usage

The project provides a `playground` command-line tool to manage the Localstack Playground environment.

```
usage: playground [-h] {up,down,reset,localstack,postgres,oracle,mysql} ...

Manage the Localstack Playground

positional arguments:
  {up,down,reset,localstack,postgres,oracle,mysql}
                        Subcommand to run
    up                  Start Localstack and all databases
    down                Stop all playground services
    reset               Reset the playground (stop services and remove volumes)
    localstack          Start only Localstack
    postgres            Start Localstack and the PostgreSQL database
    oracle              Start Localstack and the Oracle database
    mysql               Start MySQL service only

options:
  -h, --help            show this help message and exit
  ```

## Configuration

By default when starting any of the database engine localstack-playground loads scripts from [Chinook Database](https://github.com/lerocha/chinook-database_) and open source database. 

Localstack Playground allows you to override that behavior and use your own custom database initialization scripts.  This is done by setting environment variables. These variables point to paths containing the SQL scripts that will be run when the databases first started. 

### Environment Variables

- **POSTGRES_INIT_PATH**: Path to the folder containing PostgreSQL initialization scripts.
- **ORACLE_INIT_PATH**: Path to the folder containing Oracle initialization scripts.
- **MYSQL_INIT_PATH**: Path to the folder containing MySQL initialization scripts.

For example, to use your custom Postgres initialization scripts, you can set the environment variable before running the command:

```bash
export POSTGRES_INIT_PATH=/path/to/postgres/scripts
playground postgres
```

If these environment variables are not set, the default scripts included with the playground will be used.

## Development

### Running Tests

You can run tests using `pytest`:

```bash
pytest tests
```

### Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact the author:

- **Author**: Daniel Repik
- **Email**: danrepik@icloud.com
```
