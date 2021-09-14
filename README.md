# Zencastr API

Quickstart
----------

```bash
$ git clone git@github.com:taxtgg/zencastr.git
$ pipenv install 
$ pipenv shell
$ pipenv install -e .
```
To configure git run:
```bash
$ pipenv run dev-init
```

To start local environment run:
```bash
$ pipenv run dev-start
$ uvicorn main:app --reload
```
Stop local dev environment by using **CTRL-C** and:
```bash
$ pipenv run dev-stop
```

Run tests:
```bash
$ pipenv run test
```

Deploy to k8s (see minikube setup [here](https://minikube.sigs.k8s.io/docs/start/)):
```bash
$ kubectl config use-context minikube
$ kubectl apply -f k8s/db.yaml
$ kubectl apply -f k8s/app.yaml
```

Access the app:
```bash
kubectl port-forward svc/zencastr 8080:80
```

The Swagger is on URL `/docs`. Enjoy!