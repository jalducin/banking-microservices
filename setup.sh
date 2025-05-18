#!/usr/bin/env bash

# Script de instalación y arranque de microservicios

# 1. Construir imágenes Docker
echo "Construyendo imágenes Docker..."
docker-compose build

# 2. Iniciar servicios en segundo plano
echo "Levantando servicios..."
docker-compose up -d

# 3. Mostrar estado de los servicios
echo "Servicios en ejecución:"
docker-compose ps
