# cloudru-devops-task

(Основная задача)[https://github.com/devopscloudrucamp/tasks]
# Description
Веб-приложение на Python предоставляет HTTP API с тремя методами для получения информации о хосте, авторе и идентификаторе пользователя.

Image mega6obep/cloudru-app

**Примечания**: 
Дополнительно создал енв для среды приложения, а то без него чего то нехватает.

Dockerfile создан как будто планируется собирать пакеты, к сожалению в приложении нет каких то внешних пакетов, но я оставил такой подход (т.к в реальных проектах они всегда есть)

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

### How check manifest?
Create namespace
```bash
kubectl create namespace cloudru
```

Create app in k8s
```bash
cd manifest
kubectl apply -f deployment.yaml
kubectl apply -f configmap.yaml
kubectl apply -f service
```


Create app in k8s from helm
```bash
helm install cloudru-app ./helm -f helm/values/development.yaml
or
helm upgrade cloudru-app ./helm -f helm/values/development.yaml
```


