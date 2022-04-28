
import argparse
import subprocess

# running `poetry run up` for up server
def up():
    cmd = ["uvicorn", "flyer.main:app", "--reload"]
    subprocess.run(cmd)

# running `poetry run t` for run parallel-tests
def t():
    cmd = ["pytest", "--workers", "8", "--tests-per-worker", "12"]
    subprocess.run(cmd)
