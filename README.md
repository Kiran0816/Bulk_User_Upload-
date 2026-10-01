# Bulk User Upload Engine & Ingestion Pipeline

A robust, high-performance web service and data ingestion pipeline built with **Flask**, **SQLAlchemy**, and **OpenPyXL** for parsing, validating, and ingesting user records from Excel spreadsheets (`.xlsx`) into relational databases (PostgreSQL / SQLite).

---

## Key Features

- **Bulk Excel Ingestion**: Streamlined parsing and ingestion of 15-attribute user datasets via `.xlsx` spreadsheets.
- **Dynamic Template Generation**: Generates standardized `.xlsx` download templates dynamically with required column schemas.
- **Granular Validation & Error Tracking**:
  - Validates required fields, data formats, and unique constraints.
  - Automatically coerces and parses datetime formats and integer identifiers.
  - Skips empty or trailing ghost rows commonly found in Excel files.
  - Returns row-level diagnostic messages (exact row index and reason for rejection) without aborting valid rows.
- **Robust Database Abstraction**: Compatible with PostgreSQL and SQLite (fallback / local dev).
- **Dual Output Support**: Returns HTML rendered templates for interactive web forms and structured JSON for REST API integrations.
- **High Test Coverage**: 100% test coverage across endpoint routes, error boundaries, and edge cases.

---

## Quantitative Benchmarks

Empirical performance measurements collected across various batch sizes:

| Batch Size | Spreadsheet Size | Processing Time | Throughput | Avg Latency / Record | Error Detection |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **50 rows** | 8.5 KB | 0.194 s | 258 rec/s | 3.87 ms | 100% (2/2) |
| **100 rows** | 11.8 KB | 0.352 s | 284 rec/s | 3.52 ms | 100% (5/5) |
| **250 rows** | 21.7 KB | 0.926 s | 270 rec/s | 3.71 ms | 100% (12/12) |
| **500 rows** | 38.0 KB | 1.900 s | 263 rec/s | 3.80 ms | 100% (25/25) |
| **1,000 rows** | 70.4 KB | 3.820 s | 262 rec/s | 3.82 ms | 100% (50/50) |

### Transaction Optimization Impact
- **Baseline (Row-by-Row Commit)**: 3.001 s (333.2 rec/s, 3.00 ms/record).
- **Batched Bulk Commit**: 0.067 s (**14,946 rec/s**, 0.07 ms/record).
- **Optimization Result**: **44.9x speedup** with a **97.8% reduction in write latency**.

---

## Project Structure

```text
bulk-user-upload/
├── app.py                  # Main Flask application and API route controllers
├── database_setup.py       # Database configuration, connection logic & User model
├── benchmark.py            # Automated performance & stress benchmarking suite
├── create_tables.sql       # PostgreSQL DDL table definitions
├── setup_database.py       # Database initialization helper script
├── templates/
│   ├── index.html          # Web UI for upload and template download
│   └── upload_result.html  # Results template showing counts & row errors
├── tests/
│   └── test_bulk_upload.py # Pytest test suite covering endpoints & error edge cases
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## Getting Started

### 1. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/bulk-user-upload.git
cd bulk-user-upload

# Create and activate virtual environment (optional)
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 2. Configure Database

By default, the application runs with SQLite for effortless local development. To use PostgreSQL:

```bash
# Set your PostgreSQL connection string in the environment
export DATABASE_URL="postgresql://username:password@localhost:5432/UserData"
# On Windows PowerShell:
$env:DATABASE_URL="postgresql://username:password@localhost:5432/UserData"
```

### 3. Run the Application

```bash
python app.py
```

The web interface will be available at `http://127.0.0.1:5000/`.

---

## Running Tests & Benchmarks

### Run Pytest Test Suite

```bash
pytest tests/ -v
```

### Run Performance Benchmarks

```bash
python benchmark.py
```

---

## API Endpoints

- `GET /` — Web interface for file upload and template download.
- `GET /api/download/template` — Generates and downloads the standardized `.xlsx` upload template.
- `POST /api/upload/users` — Multipart form-data upload endpoint. Accepts `.xlsx` files and returns upload metrics and row-level validation results. Supports `Accept: application/json` for REST clients.
