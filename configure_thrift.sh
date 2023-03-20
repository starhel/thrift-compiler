set -x

SRC="$1"
PREFIX="$2"

cd "$SRC" || exit
./bootstrap.sh
./configure --disable-libs --prefix "$PREFIX"
