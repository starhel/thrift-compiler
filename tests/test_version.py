import subprocess


def test_compile(tmp_path):
    stdout = subprocess.check_output(["thrift", "-version"])
    assert stdout.strip() == b'Thrift version 0.13.0'

