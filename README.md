

## Overview

The Indian Premier League (IPL), founded in 2008, is a premier Twenty20 (T20) cricket league that has captivated audiences worldwide. This project offers an in-depth analysis of the IPL, spanning from its inception to the 2024 season. By leveraging the latest and most comprehensive IPL dataset, the analysis delves into match statistics, player performances, team comparisons, and much more.

## Table of Contents

- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Analysis and Insights](#analysis-and-insights)
  - [Matches Per Season](#matches-per-season)
  - [Venue-wise Match Distribution](#venue-wise-match-distribution)
  - [Team Performance](#team-performance)
  - [Top Players](#top-players)
  - [Toss Analysis](#toss-analysis)
  - [Batsman Analysis](#batsman-analysis)
  - [Bowler Analysis](#bowler-analysis)
- [Tools & Libraries Used](#tools--libraries-used)
- [Acknowledgements](#acknowledgements)


## About the Project

This project provides a detailed exploration of IPL matches and player performances over the years. It aims to uncover trends, patterns, and insights that can help fans, analysts, and teams better understand the dynamics of the game. From the number of matches played each season to the most prolific players, this analysis covers it all.

## Dataset

The dataset used in this project consists of two CSV files: `matches_2008-2024.csv` and `deliveries_2008-2024.csv`. These files contain detailed information on match summaries and ball-by-ball data.

- **[IPL Complete Dataset (2008-2024)](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)**

## Analysis and Insights

### Matches Per Season

- Analysis of the number of matches played each season, revealing trends and changes over time.

### Venue-wise Match Distribution

- Examination of the number of matches played across different venues, highlighting the most popular and frequently used stadiums.

### Team Performance

- Insights into the number of matches played by each team and their win-loss records across different seasons.

### Top Players

- Identification of top-performing players based on metrics like "Player of the Match" awards, runs scored, wickets taken, etc.

### Toss Analysis

- Analyzing how winning the toss impacts match outcomes and exploring any correlation between toss results and match wins.

### Batsman Analysis

- Detailed analysis of batting performance, including the number of 4s, 6s, top run-scorers, and milestone achievements like half-centuries and centuries.

### Bowler Analysis

- In-depth examination of bowler performance, including the most common types of dismissals and leading wicket-takers.

## Tools & Libraries Used

- **Python**
- **Numpy**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **Plotly**

## Acknowledgements

- **IPL Complete Dataset (2008-2024)**: The dataset used in this analysis is sourced from Kaggle and is up-to-date through the 2024 season. Available [here](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020).



## Getting Started

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd ipl-analytics-main
```

### 2. Install Dependencies
We recommend using a virtual environment.
```bash
pip install -r requirements.txt
```

### 3. Data Files
- `matches_2008-2024.csv` should be present in the project folder.
- **You do NOT need to manually download `deliveries_2008-2024.csv`.**
  - If this file is missing, it will be automatically downloaded from Google Drive the first time you run the code, using the [gdown](https://github.com/wkentaro/gdown) package.
  - The download link is: [Google Drive File](https://drive.google.com/file/d/1-HRYfJVaoAheSTH6sje3U9Sk-p3cuqJo/view?usp=sharing)

### 4. How the Large File is Handled
- When you run the project, if `deliveries_2008-2024.csv` is not found, the code will:
  1. Check for `gdown` and install it if needed.
  2. Download the file directly from Google Drive.
- This ensures you always have the latest data without manual steps.

### 5. Running the Project
- For Streamlit apps:
  ```bash
  streamlit run app.py
  ```
- For Jupyter/Colab notebooks, open the notebook and run the cells as usual.
- For scripts, run with:
  ```bash
  python script_name.py
  ```

## Project Structure
- `app.py` – Main Streamlit app
- `datasetPreprocessing.py` – Data loading and cleaning (handles auto-download of large CSV)
- `exploratoryDataAnalysis.py`, `teamAnalysis.py`, etc. – Analysis modules
- `Datasets/` – Contains `matches_2008-2024.csv` (do not add `deliveries_2008-2024.csv` manually)

## Requirements
- Python 3.7+
- pandas, numpy, matplotlib, seaborn, plotly, streamlit, gdown, etc.

## Notes
- If you delete `deliveries_2008-2024.csv`, it will be re-downloaded automatically next time you run the code.
- No need to manually manage large files—everything is handled in code for your convenience.

## Acknowledgements
- IPL dataset: [Kaggle IPL Complete Dataset (2008-2024)](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020)
- Google Drive file for large deliveries data: [here](https://drive.google.com/file/d/1-HRYfJVaoAheSTH6sje3U9Sk-p3cuqJo/view?usp=sharing)

## Enjoy exploring IPL analytics!
