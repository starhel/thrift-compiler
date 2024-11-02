#!/usr/bin/env bash

set -x

SRC="$1"
PREFIX="$2"

cd "$SRC" || exit
autoconf --version
autoreconf -i
./bootstrap.sh
./configure --disable-debug --disable-libs --prefix "$PREFIX"
