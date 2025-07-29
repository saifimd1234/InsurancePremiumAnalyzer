# 📊 InsurancePremiumTrendAnalyzer

This project automates the extraction and analysis of **Gross Direct Premium** data from quarterly insurance PDFs filed by insurance companies (Form NL-4 – Premium Schedule). It enables quick conversion of unstructured financial PDFs into structured data for analytics and trend visualization.

---

## 🧾 Problem Statement

Insurance companies submit quarterly reports in PDF format containing financial schedules such as **FORM NL-4**. Manually extracting the premium information from each file is inefficient and time-consuming.

This tool automates the process by:
- Extracting **Health**, **Personal Accident**, **Travel**, and **Total Gross Direct Premium** values
- Mapping them with the correct **quarter** and **insurance provider**
- Saving the output into a structured **CSV**
- (Optional) Plotting trendlines over time per provider

---

## ✅ Features

- 🔍 Extracts premium data from multiple quarterly PDFs
- 📅 Automatically detects quarter and year
- 🏢 Identifies the insurance provider
- 💾 Saves extracted data in clean `.csv` format
- 📈 Supports trendline plotting for analytics (per provider)
- ⚙️ Modular and easy to extend

---

## 📁 Project Structure

InsurancePremiumTrendAnalyzer/  
├── data/ # Folder to place input PDF files    
│ ├── Q1_2023.pdf  
│ └── ...  
├── output/ # Folder for CSV and images  
│ ├── extracted_premium.csv  
│ └── trendline_aditya_birla.png  
├── extract_premium.py # Main extraction script  
├── requirements.txt # Python dependencies  
└── README.md # Project description  
  
---

## 🚀 How It Works

1. The script reads all `.pdf` files from the `data/` folder.
2. It searches each file for the **FORM NL-4 - PREMIUM SCHEDULE** section.
3. It extracts:
   - Insurance provider name
   - Quarter and year
   - Gross Direct Premium (Health, Personal Accident, Travel, Total)
4. It stores all extracted data in a structured CSV file.
5. (Optional) It can plot trendlines of premium data for analytics.

---

## 🧠 Use Case

This tool is especially useful in contexts where insurance companies, regulators, or analysts need to process and analyze structured financial data from quarterly PDF disclosures.

### 📌 Who Can Use This?

- **Insurance Data Analysts** – Quickly extract and analyze premium trends across quarters.
- **Financial Reporting Teams** – Automate reporting pipelines that depend on raw PDF disclosures.
- **Regulators & Auditors** – Validate and compare gross premium data across multiple providers.
- **Business Intelligence Teams** – Feed cleaned data into dashboards for stakeholder reporting.
- **Actuarial & Planning Teams** – Use structured premium data for pricing models and forecasting.
- **Competitor Researchers** – Track premium growth of rival insurers over time.

### 💼 Practical Applications

- Automating the extraction of **FORM NL-4 Premium Schedule** data from PDFs
- Creating a time-series dataset for premium-related analytics
- Comparing premium performance between insurance providers
- Feeding cleaned data into Excel, Tableau, Power BI, or Jupyter dashboards
- Reducing human error and manual work in financial data processing

Absolutely! Below is a **complete `README.md` file** focused specifically on **"How to Run the Project"**, with everything included from installation to execution — ready to copy and paste:

---

# 🖥 How to Run the Project – InsurancePremiumTrendAnalyzer

This guide helps you set up and run the **InsurancePremiumTrendAnalyzer**, a Python-based tool that extracts Gross Direct Premium data from quarterly insurance PDF reports (Form NL-4 – Premium Schedule), and saves it to a structured CSV for analysis.

---

## ✅ Prerequisites

- Python 3.7 or above installed  
- Internet connection (to install packages)
- Quarterly insurance PDFs with **FORM NL-4** present in them

---

## 📦 Step 1: Install Required Packages

Make sure you're in your project directory. Then install dependencies using:

```bash
pip install -r requirements.txt
````

### requirements.txt should include:

```txt
pdfplumber
pandas
matplotlib
```

This will install:

* `pdfplumber` – to extract structured text and tables from PDFs
* `pandas` – to organize data into a structured DataFrame
* `matplotlib` – to plot trendline graphs

---

## 📁 Step 2: Add Your PDF Files

Place all the quarterly PDF files into the `data/` folder inside your project.

📂 Example:

```
InsurancePremiumTrendAnalyzer/
├── data/
│   ├── Q1_2023.pdf
│   ├── Q2_2023.pdf
│   └── Q1_2024.pdf
```

Each file should contain the **FORM NL-4 – PREMIUM SCHEDULE** section for accurate extraction.

---

## ▶️ Step 3: Run the Extraction Script

From the terminal or command prompt, run:

```bash
python extract_premium.py
```

This script will:

* Extract provider name, quarter, and gross direct premium values
* Save the structured results into:

```
output/extracted_premium.csv
```

If plotting is enabled in the script, trendline images will also be saved to:

```
output/trendline_<provider>.png
```

---

## 📊 Output Example

### ✅ CSV Output:

| Provider                                  | Quarter | Health | Personal Accident | Travel | Total Premium |
| ----------------------------------------- | ------- | ------ | ----------------- | ------ | ------------- |
| Aditya Birla Health Insurance Co. Limited | Q1 2025 | 96804  | 5664              | 1591   | 104059        |

### 📈 Trendline (Optional):

* A line chart showing premium growth over quarters for each provider
* Saved as PNG in the `output/` folder

---

## 🔁 Repeat

To analyze more data:

* Add additional PDFs into `data/`
* Re-run the script

---

## 🙋 Need Help?

If your PDFs follow a different format or aren't extracting correctly:

* Open the PDF manually and confirm it contains **"FORM NL-4"**
* You may need to adjust the regular expressions inside `extract_premium.py` to match that structure

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.

## 🌟 About Me

Hi there! I’m **Mohammad Saifi**, a passionate **Data Scientist** and recent graduate eager to contribute to the world of data-driven solutions. As a fresher, I’m focused on building scalable data pipelines, designing efficient data models, and deriving actionable insights through analytics. My goal is to leverage my skills in SQL, data engineering, and machine learning to solve real-world problems and grow in the field of data science.

Let's stay in touch! Feel free to connect with me on the following platforms:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/saifimd1234)  
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/saifimd1234)
[![Website](https://img.shields.io/badge/Website-000000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://saifi.live)
