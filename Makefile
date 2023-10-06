PYTHON = python
PYTEST = pytest
TEST_FILE = challenge2/tests/test_print_transfers.py

run-challenge1:
	$(PYTHON) challenge1/string_compression_task.py

run-challenge1b:
	$(PYTHON) challenge1/network_failure_point_task.py

run:
	PYTHONPATH=. $(PYTHON) challenge2/transaction_logs.py

test:
	PYTHONPATH=. $(PYTEST) $(TEST_FILE)
