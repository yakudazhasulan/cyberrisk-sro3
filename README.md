\# CyberRisk SRO №3



Docker Compose project — Team 2.



\## Project Description



This project demonstrates containerization of web applications

using Docker, Docker Compose, Nginx, Flask, PostgreSQL and MySQL.



\## Project Structure



\- task1 — Static website using Nginx

\- task2 — Flask application with PostgreSQL

\- task3 — Flask application with MySQL



\## Technologies



\- Docker

\- Docker Compose

\- Nginx

\- Python / Flask

\- PostgreSQL 16

\- MySQL 8.4



\## Applications



| Task | Application | Local URL |

|------|-------------|-----------|

| 1 | Nginx Website | http://localhost:8080 |

| 2 | Flask + PostgreSQL | http://localhost:5000 |

| 3 | Flask + MySQL | http://localhost:5001 |



\## How to Run



Install Docker Desktop.



For Task 1:



```bash

cd task1

docker compose up -d --build

```



For Task 2 and Task 3:



Create a `.env` file in each task directory and configure

the required database passwords before starting.



```bash

cd task2

docker compose up -d --build

```



```bash

cd task3

docker compose up -d --build

```



\## Docker Hub



\- \[Nginx Website](https://hub.docker.com/r/zhandullaev/cyberrisk-site)

\- \[Flask + PostgreSQL](https://hub.docker.com/r/zhandullaev/cyberrisk-postgres-app)

\- \[Flask + MySQL](https://hub.docker.com/r/zhandullaev/cyberrisk-mysql-app)



\## Security



Environment files containing database passwords are excluded

from Git using `.gitignore`.

