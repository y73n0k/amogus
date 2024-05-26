export COMPOSE_FILES="$(find . -iname 'docker-compose.yaml')"
for COMPOSE_FILE in $COMPOSE_FILES
do
    cd $(dirname $COMPOSE_FILE)
    docker compose up -d --build
    cd $OLDPWD
done
