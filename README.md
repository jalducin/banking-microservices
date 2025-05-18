# Banking Microservices Platform

Este proyecto es una plataforma de microservicios bancarios implementada con **FastAPI**.
Proporciona distintos servicios independientes para gestión de préstamos, cuentas, pagos, riesgos y notificaciones.

## Estructura del proyecto

```
banking-microservices/
├── api-gateway/            # Gateway y autenticación
├── loans-service/          # Servicio de préstamos
├── accounts-service/       # Servicio de cuentas
├── payments-service/       # Servicio de pagos
├── risk-service/           # Servicio de evaluación de riesgo
├── notifier-service/       # Servicio de notificaciones
├── docker-compose.yml      # Orquestación de servicios
├── requirements.txt        # Dependencias Python comunes
├── setup.sh                # Script Bash para Linux/macOS
├── setup.bat               # Script Batch para Windows CMD
└── setup.ps1               # Script PowerShell para Windows PowerShell
```

## Prerrequisitos

* Docker & Docker Compose
* Python 3.8+
* Bash (Linux/macOS) o PowerShell/CMD (Windows)

## Requerimientos Python

Para centralizar dependencias, hemos creado un archivo raíz `requirements.txt` con las librerías comunes:

```bash
fastapi
uvicorn[standard]
pydantic
httpx
python-jose
scikit-learn
pytest
```

Si prefieres gestionar dependencias por servicio, copia `requirements.txt` dentro de cada carpeta de servicio y renómbralo según su dominio:

```
loans-service/requirements.txt
accounts-service/requirements.txt
payments-service/requirements.txt
risk-service/requirements.txt
notifier-service/requirements.txt
```

Instala las dependencias de todo el proyecto de una sola vez:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

O bien, instala solo las de un servicio:

```bash
cd loans-service
pip install -r requirements.txt
```

## Instalación y arranque

### Con Docker Compose

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/banking-microservices.git
   cd banking-microservices
   ```
2. (Opcional pero recomendado) Genera explícitamente los contenedores antes de iniciar:

   ```bash
   docker-compose build
   ```
3. Arranca todos los servicios en segundo plano y fuerza la reconstrucción si cambiaste algo:

   ```bash
   docker-compose up -d --build
   ```
4. Verifica el estado de los servicios:

   ```bash
   docker-compose ps
   ```

> **Nota Windows:** Si usas Docker Desktop en Windows, asegúrate de que el motor Linux esté activo y ejecuta estos comandos en PowerShell o CMD con privilegios de administrador. En caso de error con `docker-compose`, prueba con la nueva sintaxis:
>
> ````powershell
> docker compose build
> docker compose up -d --build
> docker compose ps
> ```### Con scripts de ayuda
> ````

* En Linux/macOS:

  ```bash
  chmod +x setup.sh
  ./setup.sh
  ```

* En Windows CMD:

  ```batch
  setup.bat
  ```

* En PowerShell (ejecutar con permisos adecuados):

  ```powershell
  ./setup.ps1
  ```

## Documentación automática

Accede a la documentación OpenAPI de cada servicio:

* API Gateway: `http://localhost:8000/docs`
* Loans Service: `http://localhost:8001/docs`
* Accounts Service: `http://localhost:8002/docs`
* Payments Service: `http://localhost:8003/docs`
* Risk Service: `http://localhost:8004/docs`
* Notifier Service: `http://localhost:8005/docs`

## Desarrollo

* Modifica el código en cada carpeta de servicio (`app/` subcarpetas).
* Para reconstruir un servicio específico:

  ```bash
  docker-compose build <service-name>
  docker-compose up -d <service-name>
  ```

## Licencia

Este proyecto es de uso educativo y de práctica personal.
