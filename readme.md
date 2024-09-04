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

The project provides a `playground` command-line tool to manage the Localstack Playground environment. The tool supports multiple subcommands to control various services.

### Starting All Services

To start Localstack and all the database services:

```bash
playground up
```

### Stopping All Services

To stop all services:

```bash
playground down
```

### Resetting the Environment

To stop all services and remove the database volumes:

```bash
playground reset
```

### Starting Individual Services

You can start individual services like Localstack, Postgres, Oracle, or MySQL.

- **Start Localstack**:
    ```bash
    playground localstack
    ```

- **Start Postgres**:
    ```bash
    playground postgres
    ```

- **Start Oracle**:
    ```bash
    playground oracle
    ```

- **Start MySQL**:
    ```bash
    playground mysql
    ```

## Configuration

Localstack Playground allows you to use custom database initialization scripts by setting environment variables. These variables point to the folder containing the SQL scripts that will be run when the databases are started. If not provided, the playground will use default initialization scripts.

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

This version of the `README.md` now includes instructions for installing the `localstack-playground` package directly from PyPI, making it easier for users to get started.