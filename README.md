# Cyber Threat Intelligence Feeds data gathering

Python scripts to automate daily data collection from CTI feeds APIs and stored in PostgreSQL.

## Setup

**Usage:**

```bash
python main.py [feeds | server]
```

**feeds:** - Fetch data from CTI feeds and store it into database.

**server:** - Start Flask App server.

**Example:**

```bash
python main.py feeds
python main.py server
```
