# LEARNING GKE
#### Build & deploy app basic-service-app
> This app demonstrates 3 microservices
> The client connects to both internal services user-service, order-service
> The client is the only service available publicly via an external load balancer
[GCP quickstart for reference](https://cloud.google.com/kubernetes-engine/docs/quickstarts/deploy-app-container-image#python)
## Deployment
### Create Artifact Registry Repo
```bash
gcloud artifacts repositories create basic-service-app \
    --project=PROJECT_ID \
    --repository-format=docker \
    --location=us-central1 \
    --description="Docker repository"
```
### Build Each Directory & Service In Order
> update PROJECT_ID to your project ID
user-service, order-service, client-service
```bash
gcloud builds submit --tag us-central1-docker.pkg.dev/PROJECT_ID/basic-service-app/{service-name} .
```

### Create kubernetes deployments & services
> within each directory user-service, order-service, client-service create
```bash
kubectl apply -f *-deployment.yaml
```
> create each service
```bash
kubectl apply -f *-service.yaml
```

### Finally create service load-balancer
> This is the only service that exposes the app externally over http
> from within the client-service directory run
```bash
kubectl apply -f clientService-service-loadBalancer.yaml
```

### Test the app locally
```bash
kubectl get services
```
Example:
![alt text](https://github.com/tlgevers/learning-gke/blob/main/example-images/image1.png?raw=true)

> copy the external IP for TYPE LoadBalancer named client-service-lb
> use curl to access the service
> NOTE: **your IP will be different**
```bash
curl http://34.27.36.71/data/123
```
Example:
![alt text](https://github.com/tlgevers/learning-gke/blob/main/example-images/image2.png?raw=true)

