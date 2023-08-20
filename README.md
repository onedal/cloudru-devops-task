# cloudru-devops-task

(Основная задача)[https://github.com/devopscloudrucamp/tasks]
# Description
Веб-приложение на Python предоставляет HTTP API с тремя методами для получения информации о хосте, авторе и идентификаторе пользователя.

**Примечания**: Dockerfile создан как будто планируется собирать пакеты, к сожалению в приложении нет каких то внешних пакетов, но я оставил такой подход (т.к в реальных проектах они всегда есть)
### How start local
```bash
cd app
docker build -t app .
docker run -p 8000:8000 --env-file .env.example app
```

### How push in docker hub
```bash
cd app
docker build -t mega6obep/cloudru-app:latest .
docker login
docker push mega6obep/cloudru-app:latest
```

Image mega6obep/cloudru-app