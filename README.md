# Weekly Crypto Price Logger

This project is a simple Python script to fetch and log the current Bitcoin price (in USD) from the CoinGecko API. It is designed to run automatically on GitHub Actions once a week or manually on demand.

---

## Features

- Fetches live Bitcoin price using CoinGecko’s public API
- Logs the current UTC timestamp alongside the price
- Runs on GitHub Actions on a scheduled basis or manual trigger

---

## Files

- `get_price.py` — Python script to fetch and print the Bitcoin price
- `requirements.txt` — Python dependencies
- `.github/workflows/weekly_crypto_price_logger.yml` — GitHub Actions workflow to run the script manually

---

## How to run locally

1. Make sure you have Python 3.11+ installed
2. Clone the repo and navigate to the folder
3. Create and activate a virtual environment:

   On **Linux/macOS**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
    ```

    On **Windows**:
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1

4. Install dependencies
    ```bash
   pip install -r requirements.txt
    ```

5. Run the script
    ```bash
   python get_price.py
    ```
    - You should see output like:
        ```
        [2025-05-27T12:00:00.000000 UTC] Bitcoin price: $27123.45
        ```


## GitHub Actions Workflow: Weekly Crypto Price Logger
This project includes a GitHub Actions workflow that automates fetching and logging the Bitcoin price. The workflow demonstrates how to use GitHub Actions for scheduling and automation of Python scripts.

### Workflow Overview
The workflow is defined in `.github/workflows/price.yml` and consists of:

- Manual Trigger (workflow_dispatch): You can run the workflow on demand from the GitHub Actions UI.

- Job Steps:
    - Checkout code: Uses actions/checkout@v4 to access the repository files.
    - Set up Python: Uses actions/setup-python@v5 to install Python 3.11.
    - Install dependencies: Installs packages from requirements.txt (e.g., requests, PyYAML).
    - Run script: Executes `get_price.p`y to fetch and log the current Bitcoin price.

### How to Run the Workflow Manually
- Go to this repository’s Actions tab.
- Select the Weekly Crypto Price Logger workflow.
- Click Run workflow to trigger it manually.

### Notes
The workflow previously included a schedule to run automatically every Sunday at midnight UTC, but this was removed to allow manual runs only.

This setup serves as an introduction to using GitHub Actions to automate Python scripts and can be extended to scheduled runs, notifications, or more complex pipelines.