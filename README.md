# Spotify Data Analyst Project

A data analytics pipeline and visualization project that extracts track details from the Spotify API, stores the data in a MySQL database, performs exploratory data analysis (EDA) using Python (Pandas, Matplotlib, Seaborn), and features an interactive Power BI dashboard.

## 📌 Project Overview

This project implements an end-to-end data analysis workflow:
1. **Data Extraction:** Connects to the Spotify Web API using the `spotipy` library to fetch track metadata (Track Name, Artist, Duration, Release Date, Playability, Disc Number, and Type).
2. **Data Storage:** Inserts the raw data into a local MySQL database for persistent storage and exports it to CSV and Excel formats.
3. **Exploratory Data Analysis (EDA):** Uses Python (`pandas`, `matplotlib`, `seaborn`) to analyze popularity distributions, correlations between duration and popularity, and top artist distributions.
4. **Data Visualization:** Employs Power BI (`Spotify.pbix`) with a custom theme (`Spotify_Theme.json`) to build interactive visual reports.

---

## 📁 Repository Structure

```text
├── Spotify.csv             # Exported dataset in CSV format
├── Spotify.xlsx            # Exported dataset in Excel format
├── Spotify.pbix            # Power BI dashboard file
├── Spotify_Theme.json      # Custom theme file for Power BI dashboard
├── Spotify_data.sql        # MySQL database schema setup script
├── spotifyconnect.py       # Python script for Spotify API extraction & MySQL insertion
├── spotify_visuals.py      # Python script for data visualizations and EDA
├── details.txt             # Example JSON response structure from Spotify API
└── screenshot/             # Screenshots of the Power BI dashboard and visuals
```

---

## 🛠️ Tech Stack & Requirements

- **Programming Language:** Python 3.x
- **Libraries:**
  - `spotipy` (Spotify API Client)
  - `mysql-connector-python` (MySQL Database Connector)
  - `pandas` (Data manipulation)
  - `openpyxl` (Excel file support)
  - `matplotlib` & `seaborn` (Data visualization)
- **Database:** MySQL
- **BI Tool:** Power BI Desktop

---

## 🚀 Getting Started

### 1. Database Setup
Ensure you have MySQL installed and running. Execute the SQL commands in `Spotify_data.sql` to initialize the database and table schema:
```sql
CREATE DATABASE spotify_db;
USE spotify_db;

CREATE TABLE spotify_entity (
    Track_Name VARCHAR(30),
    Artists_Name VARCHAR(30),
    Duration FLOAT,
    Album_Id VARCHAR(40),
    ReleaseDate DATE,
    Playable BOOLEAN,
    Disc_Number INT,
    Track_Type VARCHAR(10),
    Popularity INT
);
```

### 2. Spotify Credentials Setup
Register an application on the [Spotify Developer Dashboard](https://developer.spotify.com/) to obtain your client credentials:
- `client_id`
- `client_secret`

Replace the placeholders in `spotifyconnect.py` with your credentials, or set them as environment variables.

### 3. Running Data Extraction
Add Spotify track URLs/IDs (one per line) to a file named `trace.txt` in the root directory. Then execute the extraction script:
```bash
python spotifyconnect.py
```
This will parse the tracks, insert them into the MySQL table, and can be configured to update `Spotify.csv` and `Spotify.xlsx`.

### 4. Running Python Visualizations
To perform EDA and display analysis plots, run:
```bash
python spotify_visuals.py
```

### 5. Exploring the Power BI Dashboard
Open `Spotify.pbix` in Power BI Desktop to view the interactive dashboard dashboard. The dashboard uses the custom `Spotify_Theme.json` for styling.

---

## 📊 Visualizations & Insights

Check out the `screenshot/` folder to preview the dashboard visuals and plots generated during EDA!
