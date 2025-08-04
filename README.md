# Customer Data Cleaning Project 

This project demonstrates basic data cleaning using Python for a synthetic customer dataset. The raw dataset includes issues such as missing values, duplicate records, inconsistent formatting and mixed data types.

## Dataset Files
- 'raw_customer_data.csv'
- `raw_customer_data.csv` – Original raw dataset with inconsistencies.
- `cleaned_customer_data.csv` – Cleaned version in CSV format.
- `cleaned_customer_data.xlsx` – Cleaned version in Excel format.

## Cleaning Performed

Steps and   Descriptions 
 -Removed duplicate row (Customer ID 1003) 
 -Handled Missing Values - Filled missing `Customer ID` (9999), `Name` (`Unknown`), and `Age` (with median age 32) 
 -Gender Formatting - Standardized values to `MALE` / `FEMALE` 
 -Country Formatting - Unified entries (e.g., `uk`, `U.K.` → `UNITED KINGDOM`) 
 -Date Standardization - Converted all `Signup Date` entries to `DD-MM-YYYY` 
-Column Renaming - Renamed all headers to lowercase and snake_case format 

##  Tools Used

- Python 
- Pandas Library

