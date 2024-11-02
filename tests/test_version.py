import subprocess


def test_version():
    stdout = subprocess.check_output(["thrift", "-version"])
    assert stdout.strip() == b'Thrift version 0.21.0'

