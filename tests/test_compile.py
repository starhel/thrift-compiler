import importlib
import subprocess
import sys
from textwrap import dedent


def test_compile(tmp_path):
    thrift_text = dedent("""\
        const string var_str = "1.0"
        const i32 var_int = 7
    """)

    f = tmp_path / "test.thrift"
    f.write_text(thrift_text)
    outdir = tmp_path / "out_dir"
    outdir.mkdir()

    subprocess.check_call(["thrift", "-gen", "py", '-out', str(outdir), str(f)])
    sys.path.insert(1, str(outdir))
    constants = importlib.import_module('test.constants')
    assert constants.var_str == "1.0"
    assert constants.var_int == 7
