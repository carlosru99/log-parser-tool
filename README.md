# Finance SAP Utils Recopilation
Log Parser Tool for Clarity AI technical interview
## Setup

### Requirements

* Python ^3.8+
* Poetry

### Get ready

#### Install python 3.8.10

- **Recommended:** [pyenv](https://github.com/pyenv/pyenv):

    ```bash
    $ pyenv install 3.8.10
    ```

    ```bash
    $ pyenv local 3.8.10
    ```

#### Install poetry and get into virtual environment

```bash
$ pip install poetry
```

- Install required `poetry-dotenv-plugin` python package to enable export .env into the shell

```bash
$ pip install poetry-dotenv-plugin
```
- Install needed packages defined in pyproject.toml

```bash
$ poetry install
```
- Enter Poetry's environment

```bash
$ poetry shell
```

## Usage
 - Read [RunBook](RF_Load_Runbook.md)

### Create .env file with the following estructure:

```bash
# Database info
REDSHIFT_HOST=''
REDSHIFT_PORT=''
REDSHIFT_DBNAME=''
REDSHIFT_USERNAME=<USER>      # secret
REDSHIFT_PASSWORD=<PASSWORD>  # secret

# S3 credentials
AWS_ACCESS_KEY=''
AWS_SECRET_KEY=''

# Execution fields
VERSION = ''
YEAR= ''
MONTH_TO_VALIDATE = ''
VALIDATION_FILE = ''
S3_BUCKET=''
S3_KEY=''
```