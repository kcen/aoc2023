#!/bin/sh
set -e

# build to create the dist
poetry build --without dev

# install the built package via pipx
pipx install -f dist/*.tar.gz
