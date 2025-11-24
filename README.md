# Python API Project — Docker + GitHub Actions CI/CD + Render

This project contains:

- Python FastAPI backend  
- Docker containerization  
- unittest testing  
- GitHub Actions CI/CD  
- Deploy hook to Render Cloud  

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

first create repo in github and push your changes to github
create repo fastapi-cicd in github
git init
git add .
git commit -m "Initial FastAPI CI/CD setup"
git branch -M main
git remote add origin https://github.com/<github-username>/fastapi-cicd.git
git push -u origin main

run in docker

docker build -t ghcr.io/tradnslds/python-api:latest .
docker run -p 8000:8000 fastapi-cicd


Deploy to Render- this is optional

Create a Render Web Service (Docker).
Get the Deploy Hook URL.
Add a GitHub secret called RENDER_DEPLOY_HOOK with the hook URL.
Push code → GitHub Actions triggers the deploy automatically.
