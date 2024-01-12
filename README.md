docker cp file_code id_docker:/usr/app/src
docker compose up --build --force-recreate -d
docker exec -it container_name_or_id /bin/bash
docker-compose up -d
