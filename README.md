# thrift-compiler
Python package with Thrift compiler

## Building on Ubuntu
```bash
docker build --pull -f "Dockerfile" -t thriftbuilder:latest .
docker run --user $UID --init --rm -e "CMAKE_BUILD_PARALLEL_LEVEL=17" --volume $PWD:$PWD mybuilder python3.10 -m build $PWD
docker run --user $UID --init --rm --volume $PWD:$PWD mybuilder auditwheel repair $PWD/dist/*.whl -w $PWD/wheelhouse
```