#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z authenticated-api-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

exec "$@"
