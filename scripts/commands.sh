#!/bin/sh

# O shell irá encerra a execução do script quando um comando falhar
set -e

wait_psql.sh
collectstatic.sh
migrate.sh
runserver.sh