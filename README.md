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

Improvements
------------
The list of possible improvements includes:
- Secure Mongo (Good tutorial [here](https://www.cloudytuts.com/guides/kubernetes/how-to-deploy-mongodb-on-kubernetes/))
- Unify scripts in [Click](https://click.palletsprojects.com/en/8.0.x/) based cli
- Add better health check endpoint (for example using [this](https://github.com/Kludex/fastapi-health))
- Add better DB connection testing
- Add Prometheus metrics exporter (using [this](https://pythonrepo.com/repo/stephenhillier-starlette_exporter-python-fastapi-utilities) or [this](https://pythonrepo.com/repo/trallnag-prometheus-fastapi-instrumentator-python-fastapi-utilities))
- 

 


