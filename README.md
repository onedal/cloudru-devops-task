# cloudru-devops-task

Main task [https://github.com/devopscloudrucamp/tasks]
# Description
The Python web application provides an HTTP API with three methods for getting host, author, and user ID information.

Image mega6obep/cloudru-app

**Attention**: 
Additionally, I created an env for the application environment, otherwise something is missing without it.

The Dockerfile was created as if it were planned to build packages, unfortunately there are no external packages in the application, but I left this approach (because real projects always have them)

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
```

### How work with playbook
Change public_key to own
```bash
ansible-playbook playbook/playbook.yml
```
Performance tested on ec2 Ubuntu 22.04.
