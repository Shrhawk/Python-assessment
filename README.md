# Assessment Tasks

## Getting Started

1. Clone this repository to your local machine:
```shell
git clone https://github.com/Shrhawk/Python-assessment.git
```

2. Navigate to the project directory:
```shell
cd assesment-task
```

## Challenges

### Challenge 1(a)
String Compression using Python

Run Task
```shell
make run-challenge1
```

### Challenge 1(b)
Find node with the highest connectivity.

Run Task
```shell
make run-challenge1b
```

### Challenge 2: Retrieve Transaction Logs

Retrieve transaction logs from Etherscan API.

Create and activate virtual environment:
```shell
python3 -m venv env
source env/bin/activate
```

Install Required Packages:
```shell
bash setup.sh
```
Create .env file:
```shell
cp .sample.env .env
```
Add `API_KEY` in `.env` file from [Etherscan](https://etherscan.io/myapikey).

Run Task:
```shell
make run
```

Run test cases:
```shell
make test
```
