# Azure CI/CD Portfolio

A Flask application demonstrating automated testing and deployment preparation for Microsoft Azure App Service.

## Technology
- Python 3.12
- Flask and Gunicorn
- pytest
- GitHub Actions
- Azure App Service
- Microsoft Entra OIDC authentication

## Application endpoints
- / — Application dashboard
- /health — Health check
- /api/status — Application status API

## Local setup
Create a virtual environment, install requirements.txt, and run app.py.

## Testing
Run pytest -v.

Four automated tests currently pass.

## GitHub Actions
- ci.yml runs automated tests on pushes and pull requests.
- azure-deploy.yml provides manual deployment using OIDC.

## Azure deployment requirements
GitHub secrets: AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_SUBSCRIPTION_ID.

GitHub variables: AZURE_WEBAPP_NAME, AZURE_RESOURCE_GROUP.

An active Azure subscription, an existing App Service, and a correctly configured federated identity are required.

## Current status
Application and CI implemented. Azure deployment workflow prepared, but deployment has not yet been performed.
