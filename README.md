# Step by Step
This section contains the steps with you can compile, create image and deploy the microservice.

## Creating docker image

1. Go to the root directory where the code is.
2. Create image from dockerfile.
```shell
docker build -t microsevice-challenge-1:latest .
docker image tag microsevice-challenge-1:latest jdiegobonp/microsevice-challenge-1:latest
docker push jdiegobonp/microsevice-challenge-1:latest
```
3. Testing the public image
```shell
docker run -d -p 5000:5000 --name microservice1 jdiegobonp/microsevice-challenge-1:latest
docker stop microservice1
docker rm microservice1
```

## Deploying on Kubernetes

1. Go to the root directory where the code is.
2. Execute the following commands:

```shell
kubectl apply -f ./k8s/deployment.yaml
kubectl apply -f ./k8s/service.yaml
kubectl get pods
kubectl get deploy
kubectl get service
```
3. To test the service, execute the following command:

```shell
kubectl port-forward service/service-challenge-1 5000:5000
```

4. Open a browser and put the URL http://localhost:5000
5. To clean the environment, execute the following commands:

```shell
kubectl delete -f ./k8s/deployment.yaml
kubectl delete -f ./k8s/service.yaml
```
