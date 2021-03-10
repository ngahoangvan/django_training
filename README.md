# DJANGO TRAINING

## Create Virtual Environment
- In this project, I use **Conda**

```bash
conda create -n django_training python=3.9  


conda activate django_training
```

## Install Requirement

```bash
conda install --file requirements.txt
```

## Start Project

```bash
# Create migration
python manage makemigratio

# Apply migration
python manage migrate

# Run server
python manage runserve
```

## Start Project via Docker
```bash
# build
docker-compose build

# run
docker-compose up
```

- Server will at: `127.0.0.1:8000`