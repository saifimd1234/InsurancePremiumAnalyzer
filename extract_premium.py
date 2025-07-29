import os
import re
import pdfplumber
import pandas as pd
import matplotlib.pyplot as plt

# === Folders ===
PDF_FOLDER = "data"
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
OUTPUT_CSV = os.path.join(OUTPUT_FOLDER, "extracted_premium.csv")

# === Storage ===
records = []

# === Quarter mapping by month ===
quarter_map = {
    "January": "Q4", "February": "Q4", "March": "Q4",
    "April": "Q1", "May": "Q1", "June": "Q1",
    "July": "Q2", "August": "Q2", "September": "Q2",
    "October": "Q3", "November": "Q3", "December": "Q3"
}

# === Extract from a single PDF ===
def extract_from_pdf(file_path):
    provider_name = ""
    quarter = ""
    year = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            # Detect quarter & year
            quarter_match = re.search(r"For The Quarter Ended\s+(\d{1,2}[a-z]{2})?\s*(\w+),\s*(\d{4})", text, re.IGNORECASE)
            if quarter_match:
                month = quarter_match.group(2).capitalize()
                quarter = quarter_map.get(month, "")
                year = quarter_match.group(3)

            # Detect provider name
            provider_match = re.search(r"([A-Za-z\s]+Insurance Co\. Limited)", text)
            if provider_match:
                provider_name = provider_match.group(1).strip()

            # Find Premium Table Line
            if "FORM NL-4" in text and "Gross Direct Premium" in text:
                lines = text.split("\n")
                for line in lines:
                    if "Gross Direct Premium" in line:
                        numbers = re.findall(r"[\d,]+", line)
                        if len(numbers) >= 4:
                            record = {
                                "Provider": provider_name,
                                "Quarter": f"{quarter} {year}",
                                "Health": int(numbers[0].replace(",", "")),
                                "Personal Accident": int(numbers[1].replace(",", "")),
                                "Travel": int(numbers[2].replace(",", "")),
                                "Total Premium": int(numbers[3].replace(",", ""))
                            }
                            records.append(record)
                            break  # Stop after first match

# === Run on all PDFs ===
pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]
for file in pdf_files:
    path = os.path.join(PDF_FOLDER, file)
    extract_from_pdf(path)

# === Save to CSV ===
df = pd.DataFrame(records)
df.sort_values(by=["Provider", "Quarter"], inplace=True)
df.to_csv(OUTPUT_CSV, index=False)
print(f"✅ Extracted data saved to: {OUTPUT_CSV}")

# === Plot trendlines (optional) ===
if not df.empty:
    for provider in df["Provider"].unique():
        provider_df = df[df["Provider"] == provider].copy()
        provider_df["Quarter"] = pd.Categorical(provider_df["Quarter"], ordered=True,
                                                categories=sorted(df["Quarter"].unique(), key=lambda q: (q.split()[1], q.split()[0])))
        provider_df.sort_values("Quarter", inplace=True)

        plt.figure(figsize=(10, 5))
        plt.plot(provider_df["Quarter"], provider_df["Total Premium"], marker='o', label=provider)
        plt.title(f"Gross Direct Premium Trend – {provider}")
        plt.xlabel("Quarter")
        plt.ylabel("Total Premium (Rs. Lakhs)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        img_name = os.path.join(OUTPUT_FOLDER, f"trendline_{provider.replace(' ', '_').lower()}.png")
        plt.savefig(img_name)
        print(f"📈 Saved trendline to {img_name}")
        plt.close()
else:
    print("⚠️ No data extracted.")
