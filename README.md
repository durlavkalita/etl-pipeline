# 🛠️ Python ETL Pipeline with MongoDB, Docker Compose, and Pytest

This project demonstrates a simple ETL pipeline in **pure Python** with:

- ✅ Data ingestion from a CSV file
- ✅ Transformation logic
- ✅ Load into MongoDB
- ✅ Docker Compose for zero local installs
- ✅ Unit tests with `pytest`
- ✅ (Optional) Mongo Express for visual inspection

---

## 📦 Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## 🚀 Getting Started

### 🔧 1. Build and Run the ETL Pipeline

```bash
docker-compose up --build etl-runner
```

### 🔧 2. Build and Run unit test

```bash
docker-compose run --rm test
```

### 🔧 3. Check mongodb
```bash
docker exec -it mongo mongosh
```