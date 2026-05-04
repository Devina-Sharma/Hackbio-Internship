
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Loading dataset directly to ensure bacteria_data is a valid DataFrame
bacterial_path = 'https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/bacteria.csv'
bacteria_data = pd.read_csv(bacterial_path)

# Set global visual theme
sns.set_theme(style="whitegrid")

# ==========================================
# Part 1: Distribution Plots
# ==========================================

# 1. Histogram of carb_fit
plt.figure(figsize=(8, 5))
sns.histplot(data=bacteria_data, x='carb_fit', bins=15, color="skyblue", edgecolor="black")
plt.title('Distribution of Carbapenem Fitness Levels')
plt.xlabel('Carbapenem Fitness Score')
plt.ylabel('Frequency')
plt.show()

# 2. KDE plot of cipro_fit
plt.figure(figsize=(8, 5))
sns.kdeplot(data=bacteria_data, x='cipro_fit', fill=True, color="tomato")
plt.title('KDE Plot of Ciprofloxacin Fitness')
plt.xlabel('Cipro Fitness Score')
plt.show()

# 3. Displot grouped by Phenotype
sns.displot(data=bacteria_data, x='carb_fit', hue='Phenotype', kind='kde', fill=True, palette="magma", height=5, aspect=1.2)
plt.title('Fitness Distribution: Phenotype Comparison')
plt.show()

# ==========================================
# Part 2: Relationship Plots
# ==========================================

# 1. Scatter plot using requested variables (carb vs pip) and semantic mapping
plt.figure(figsize=(10, 6))
sns.scatterplot(data=bacteria_data, x='carb_fit', y='pip_fit', hue='labels', style='Phenotype', s=100)
plt.title('Relationship: Carbapenem vs. Piperacillin Fitness')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') 
plt.show()

# 2. Line plot using requested variables (kan vs genta) and semantic mapping
plt.figure(figsize=(10, 6))
sns.lineplot(data=bacteria_data, x='kan_fit', y='genta_fit', hue='Isolation origin')
plt.title('Line Plot: Kanamycin vs. Gentamicin Fitness by Origin')
plt.show()

# ==========================================
# Part 3: Categorical Plots
# ==========================================

# 1. Bar plot grouped by labels
plt.figure(figsize=(10, 5))
sns.barplot(data=bacteria_data, x='labels', y='carb_fit', palette='muted')
plt.title('Mean Carbapenem Fitness by Label Group')
plt.xticks(rotation=45)
plt.show()

# 2. Box plot grouped by Phenotype
plt.figure(figsize=(10, 5))
sns.boxplot(data=bacteria_data, x='Phenotype', y='cipro_fit', palette='Set2')
plt.title('Distribution of Cipro Fitness by Phenotype')
plt.show()

# 3. Violin plot with Strip plot overlay for raw observation visibility
plt.figure(figsize=(12, 6))
sns.violinplot(data=bacteria_data, x='Isolation origin', y='carb_fit', inner=None, color=".9")
sns.stripplot(data=bacteria_data, x='Isolation origin', y='carb_fit', jitter=True, size=5, palette='bright')
plt.title('Raw Observations vs. Density by Isolation Origin')
plt.xticks(rotation=45)
plt.show()

# ==========================================
# Part 4: Heatmap of Fitness Values
# ==========================================

# Explicitly identifying numerical fitness columns for heatmap construction
fitness_columns = [col for col in bacteria_data.columns if '_fit' in col]
heatmap_df = bacteria_data[fitness_columns]

# Building heatmap with mandatory numerical annotations (annot=True)
plt.figure(figsize=(12, 10))
sns.heatmap(heatmap_df.head(20), annot=True, cmap='YlGnBu', fmt=".2f", cbar_kws={'label': 'Fitness Score'})
plt.title('Antibiotic Fitness Profile Heatmap (Annotated)')
plt.show()

# ==========================================
# Part 5: Faceted Categorical Plot with catplot()
# ==========================================

# Using catplot to create faceted box plots split by 'labels'
g = sns.catplot(
    data=bacteria_data, 
    x='Phenotype', 
    y='carb_fit', 
    col='labels', 
    kind='box', 
    col_wrap=3, 
    palette='pastel'
)

g.fig.subplots_adjust(top=0.85)
g.fig.suptitle('Faceted Analysis: Carb Fitness by Phenotype across Label Groups', fontsize=16)
plt.show()
