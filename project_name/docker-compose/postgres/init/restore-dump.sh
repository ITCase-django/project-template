#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

filepath="/docker-entrypoint-initdb.d/init.pg-dump"
if [[ -f $filepath ]]; then
    pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Ov "$filepath"
else
    echo "Нет дампа $filepath"
    echo "База пустая!"
fi