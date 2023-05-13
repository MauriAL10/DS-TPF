echo "Inicializando Swarm"
docker swarm init

echo "Levantamos la red y el registro"
docker service create --name registry --publish published=5000,target=5000 registry:2

echo "Iniciando creación de las imágenes"
docker build -t "tpf-master" ./masterNodeJs
docker build -t "tpf-slave-nj" ./slavesNodeJs
@REM docker build -t "tp5-slave-py" ./slavesPython
docker build -t "tpf-web-ui" ./web-ui

echo "Crear y etiquetar imágenes"
docker tag tpf-master 10.1.2.112:5000/tpf-master

docker tag tpf-slave-nj 10.1.2.112:5000/tpf-slave-nj
docker push 10.1.2.112:5000/tpf-slave-nj

@REM docker tag tp5-slave-py 10.1.2.112:5000/tp5-slave-py
@REM docker push 10.1.2.112:5000/tp5-slave-py

@REM docker tag tp5-slave-go 10.1.2.112:5000/tp5-slave-go
@REM docker push 10.1.2.112:5000/tp5-slave-go

echo "Levantar servicios master y slave"
docker stack deploy -c docker-compose.yml master_slave
