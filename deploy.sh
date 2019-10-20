#!/bin/bash

set -ex -o allexport

source ./.env

set +o allexport

docker stack deploy -c stacks/${1?"Stack file not found"} ${1%.yml}
