@echo off
REM Script de arranque para Windows con Docker Compose
echo Construyendo imágenes Docker...
docker-compose build

echo Levantando servicios...
docker-compose up -d

echo Estado de los servicios:
docker-compose ps

pause
