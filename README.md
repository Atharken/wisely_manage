# Rental Account Manager

A simple Python-based **Rental Account Manager** for storing and managing rented accounts.

This project was created as a practical Python project to practice **CSV file handling, functions, CRUD operations, date handling, phone-number validation, and exception handling**.

---

## Features

### 1. Add Rental Account

You can add a rental account with:

- Account name
- Account type
- Phone number
- Country/region
- Rental duration
- Start date
- Automatically calculated end date

The project currently provides predefined account types:

- Ultimate Xbox Game Pass
- Premium Xbox Game Pass
- Rockstar Account
- Other

---

### 2. Phone Number Validation

The project uses the Python `phonenumbers` library to:

- Parse phone numbers
- Validate phone numbers
- Convert valid numbers into international E.164 format

Example:

```text
+919812343242
```

The project also contains a region dictionary for countries such as:

- India
- United States
- United Kingdom
- Canada
- Australia
- UAE
- Saudi Arabia
- Singapore
- Germany
- France
- Japan
- China
- Pakistan
- Bangladesh
- Nepal

---

### 3. Rental Dates

When an account is added, the program records the current date automatically.

The user enters the rental duration in days.

For example:

```text
Start date: 2026-10-07
Rental period: 30 days
End date: 2026-11-06
```

The end date is calculated using Python's `timedelta`.

---

### 4. Check Due Accounts

The `due()` function checks the stored `end_date` against the current date.

Expired accounts are displayed when the program starts.

The comparison is performed by converting the CSV date string back into a Python `date` object.

---

### 5. Search Accounts

Accounts can be searched by account name.

The search is:

- Case-insensitive
- Whitespace-tolerant

For example:

```text
Athar
athar
 ATHAR
```

can match the same account name.

---

### 6. Remove Accounts

Accounts can be removed using an index.

There are currently two options:

```text
1. by search
2. by all index
```

After removing an account, the CSV file is rewritten with the updated data.

---

### 7. Edit Accounts

Existing accounts can be edited by selecting an index.

Available fields:

```text
1. account
2. type
3. number
4. date
5. end_date
```

The updated information is then saved back to the CSV file.

---

## Technologies Used

- **Python**
- **CSV**
- **Pathlib**
- **datetime**
- **phonenumbers**

Python modules used:

```python
import csv
from pathlib import Path
import phonenumbers
from phonenumbers import PhoneNumberFormat
from datetime import date, timedelta
from phonenumbers.phonenumberutil import NumberParseException
```

---

## Data Storage

The project uses a CSV file named:

```text
acc_data.csv
```

The CSV contains these fields:

```text
account
type
number
date
end_date
```

Example:

```text
account,type,number,date,end_date
Athar,ultimate xbox gamepass,+919812343242,2026-10-07,2026-11-06
```

The CSV file is automatically created if it does not already exist.

---

## Project Structure

```text
Rental-Account-Manager/
│
├── wisely.py
├── acc_data.csv
└── README.md
```

### `wisely.py`

The main Python program containing:

- Account management
- CSV operations
- Search
- Edit
- Delete
- Phone-number validation
- Date calculations
- Due-account checking

### `acc_data.csv`

Stores the rental account information.

### `README.md`

Documentation for the project.

---

## How It Works

The basic flow of the application is:

```text
        User
         │
         ▼
   Python Menu
         │
   ┌─────┼─────┐
   │     │     │
 Add   Search  Edit
   │     │     │
   └─────┼─────┘
         │
       Delete
         │
         ▼
     CSV File
```

The program loads records from the CSV file, performs the requested operation, and saves changes back to the CSV file when necessary.

---

## Main Menu

When the program starts, the following menu is displayed:

```text
1. add rent account
2. search by account
3. remove account
4. edit account
5. exit
```

### Add

Adds a new rental account.

### Search

Searches for an account by name.

### Remove

Deletes an account from the CSV file.

### Edit

Changes information about an existing account.

### Exit

Closes the program.

---

## Running the Project

### 1. Install Python

Make sure Python is installed on your system.

Check with:

```bash
python --version
```

---

### 2. Install `phonenumbers`

Run:

```bash
pip install phonenumbers
```

---

### 3. Run the program

```bash
python wisely.py
```

The program will automatically create:

```text
acc_data.csv
```

if it does not already exist.

---

## Example

Adding an account may look like:

```text
1. add rent account
2. search by account
3. remove account
4. edit account
5. exit

:1

enter your account
:Athar

enter account type
1. ultimate xbox gamepass
2. premium xbox gamepass
3. rock star account
4. others
:1
```

Then the program asks for the country, phone number, and rental duration.

The rental dates are calculated automatically.

---

## What I Practiced With This Project

This project was built to practice several Python concepts together:

- Functions
- Lists
- Dictionaries
- Loops
- `while` loops
- `if/elif` conditions
- `try/except`
- CSV files
- `csv.DictReader`
- `csv.DictWriter`
- File handling
- `pathlib.Path`
- Date and time handling
- `timedelta`
- External Python libraries
- Phone-number validation
- CRUD-style operations

---

## Future Improvements

Possible improvements for future versions:

- Better input validation
- Better handling of invalid indexes
- More country/region options
- Account duplication checks
- Better display of expired accounts
- Remaining-days calculation
- Improved edit validation
- A graphical/mobile frontend
- Convert the Python program into a REST API
- Connect the application to a mobile-friendly frontend
- Replace CSV storage with a database in a future version

---

## Author

**Mohd Athar**

BCA Student

This project was created as a Python practice/project application.
