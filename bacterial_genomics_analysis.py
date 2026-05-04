import pandas as pd

# ==========================================
# Part 1: Data Loading
# ==========================================
# Importing the bacterial dataset from the HackBio repository
bacterial_path = 'https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/bacteria.csv'
df = pd.read_csv(bacterial_path)

# Assigning to a descriptive variable name
bacteria_data = df

print('Dataset Shape:', df.shape)
print('Columns available:', df.columns.tolist())

# ==========================================
# Part 2: Data Selection & Indexing
# ==========================================
# Selecting specific row by index
row_15 = df.iloc[15]
print("\nRow 15 data details:\n", row_15)

# Extracting a specific column (Species)
species_col = df['species']
print("\nFirst 5 entries in species column:\n", species_col.head())

# Pinpointing a specific value using .loc coordinate
val_origin = df.loc[15, 'Isolation origin']
print(f"\nOrigin of sample at row 15: {val_origin}")

# ==========================================
# Part 3: Data Filtering
# ==========================================
# Filtering for bacteria with a carb_fit score higher than 0.5
carb_fit_high = df[df['carb_fit'] > 0.5]
print(f"\nFiltered high carb_fit (Total rows: {len(carb_fit_high)}):")
print(carb_fit_high.head())

# ==========================================
# Part 4: Handling Missing Data (Simulated)
# ==========================================
# Creating a working copy for data cleaning practice
bacteria_data_missing = df.copy()

# Checking for missing data across rows
missing_per_row = bacteria_data_missing.isnull().sum(axis=1)
print("\nMissing values per row (Top 5):\n", missing_per_row.head())

# Demonstration of missing data handling:
# 1. Imputing missing values with a constant (1)
bacteria_data_filled = bacteria_data_missing.fillna(1)
# 2. Removing columns containing any null values
bacteria_data_dropped_cols = bacteria_data_missing.dropna(axis=1)

# ==========================================
# Part 5: Integrity Check
# ==========================================
# Verifying if there are any actual missing values in the main dataset
any_missing = bacteria_data.isnull().values.any()
print(f"\nAre there missing values in main dataset? {any_missing}")
print("Missing values per column:\n", bacteria_data.isnull().sum())

# ==========================================
# Part 6: Data Cleaning 
# ==========================================
# Renaming coordinate columns to more descriptive UMAP labels
bacteria_data = bacteria_data.rename(columns={'C1': 'UMAP1', 'C2': 'UMAP2'})

# ==========================================
# Part 7: Sorting
# ==========================================
# Sorting by Biosafety Level (BSL) in descending order
bacteria_data = bacteria_data.sort_values(by='BSL', ascending=False)
print("\nTop 5 rows after sorting by BSL (Descending):")
print(bacteria_data[['species', 'BSL']].head())

# ==========================================
# Part 8: Grouped Analysis
# ==========================================
# Calculating average fitness scores per label group
mean_analysis = bacteria_data.groupby('labels')[['cipro_fit', 'carb_fit']].mean()
print("\nAverage antibiotic fitness by group:\n", mean_analysis)

# Finding the maximum fitness recorded per label group
max_analysis = bacteria_data.groupby('labels')[['cipro_fit', 'carb_fit']].max()
print("\nMax antibiotic fitness by group:\n", max_analysis)

# Distribution of strains across different phenotypes
phenotype_counts = bacteria_data['Phenotype'].value_counts()
print("\nCount of samples per Phenotype:\n", phenotype_counts)
