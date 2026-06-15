# 🧹 Data Handling — pandas & Missing Values

Scripts focused on **cleaning, manipulating, and repairing real-world messy data** using `pandas`. This folder covers everything from basic DataFrame operations to handling missing values with `dropna()` and `fillna()`. 📊

---

## 📦 What's Inside

| File | Description |
|---|---|
| 🗃️ **`data manupulation.py`** | Basic DataFrame operations — creating a DataFrame, adding a new column, appending a row with `.loc[]`, dropping a row, and previewing data with `.head()` / `.tail()`. |
| 🩹 **`Usuing fillna.py`** | Demonstrates filling missing (`None`) values in a salary column using the **column mean**, via `fillna(..., inplace=True)`. |
| 🧼 **`Handeling data with dropna amd fillna.py`** | A complete missing-data workflow: detect missing values with `isnull()`, count total nulls, remove rows with `dropna()`, and fill missing values **per-column** with custom defaults using `fillna({...})`. |
| 📄 **`unclean.csv`** | A real movie-dataset sample (IMDB-style) — messy on purpose! Includes encoding artifacts (`?ÿ`), missing values (`,,`), duplicate columns (`title_year` appears twice), and quoted numeric strings (`"""475"""`). Great for practicing data-cleaning techniques. |

---

## 🔍 Concept Breakdown

### 🗃️ DataFrame Basics (`data manupulation.py`)
```python
df["Experience (Years)"] = [5, 1, 2]   # add a new column
df.loc[3] = ["suvi", "Marketing", 50000, 3]  # add a new row
df = df.drop(0)                         # drop a row by index
df.head(1)  /  df.tail(1)               # preview first/last rows
```

### 🩹 Filling with Mean (`Usuing fillna.py`)
```python
df['SALARY'].fillna(df['SALARY'].mean(), inplace=True)
```
Replaces missing salary values with the **average** of the existing values — a common imputation strategy for numeric columns.

### 🧼 Detect → Remove → Fill (`Handeling data with dropna amd fillna.py`)
A 3-step missing-data workflow:
1. **Detect** → `data.isnull()` and `data.isnull().sum().sum()`
2. **Remove** → `data.dropna()` (drops any row with a missing value)
3. **Fill** → `data.fillna({col: default_value, ...})` (custom fill per column)

---

## 📄 About `unclean.csv`

A movie metadata CSV with deliberately messy real-world quirks:
- 🔤 Encoding artifacts in movie titles (`?ÿ`)
- ❓ Empty cells (e.g. `facenumber_in_poster`, `duration`)
- 🔁 Duplicate column (`title_year` listed twice)
- 🧩 Oddly quoted numbers (e.g. `"""475"""`)

Perfect for practicing `dropna()`, `fillna()`, type conversion, deduplication, and general data wrangling.

---

## 🛠️ Requirements

```bash
pip install pandas
```

## ▶️ Running

```bash
python "Usuing fillna.py"
python "Handeling data with dropna amd fillna.py"
python "data manupulation.py"
```

> 💡 Keep `unclean.csv` in this same folder if you write a script that loads it with `pd.read_csv("unclean.csv")`.

---

✨ Messy data is everywhere — these scripts are small reps for building the muscle to clean it up!
