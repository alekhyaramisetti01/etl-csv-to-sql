# 🛠️ Setting Up PostgreSQL for the ETL Project (PowerShell Users)

This guide provides step-by-step instructions to install PostgreSQL and configure it for the **ETL Data Pipeline** project using PowerShell.

---

## 📌 1️⃣ Install PostgreSQL

Download PostgreSQL from the [official website](https://www.postgresql.org/download/) and follow these steps:

1. Select your OS (Windows, macOS, or Linux).
2. Install **PostgreSQL** and **pgAdmin** (optional).
3. Remember your **username** and **password** during setup.

To verify the installation, open **PowerShell** and run:
```powershell
psql --version
```
If `psql` is not recognized, you need to add PostgreSQL to your system **PATH** (see Step 2).

---

## 📌 2️⃣ Add PostgreSQL to PowerShell PATH
If PowerShell does not recognize `psql`, add it to the system PATH manually:

1. Open **PowerShell** as Administrator.
2. Check where PostgreSQL is installed (usually `C:\Program Files\PostgreSQL\xx\bin` where `xx` is the version).
3. Add the path to the system PATH variable:
```powershell
[System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Program Files\PostgreSQL\17\bin", [System.EnvironmentVariableTarget]::Machine)
```
4. Restart PowerShell and verify:
```powershell
psql --version
```

---

## 📌 3️⃣ Start PostgreSQL Service (Windows Users)
If PostgreSQL is not running, start it manually:
```powershell
net start postgresql
```
If you get an error, try:
```powershell
Get-Service postgresql*
Start-Service -Name "postgresql-x64-15"  # Replace with your PostgreSQL version
```

---

## 📌 4️⃣ Create the Database & User

Open **PowerShell** and enter the PostgreSQL shell:
```powershell
psql -U postgres
```

Now, run the following SQL commands:

```sql
-- Create a new database
CREATE DATABASE etl_project;

-- Create a user and grant privileges
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE etl_project TO myuser;
```

📌 **Replace `myuser` and `mypassword` with your actual username and password.**

👉 **Exit PostgreSQL:**
```sql
\q
```

---

## 📌 5️⃣ Verify Connection to PostgreSQL
To check if the database was created successfully, run:
```powershell
psql -U myuser -d etl_project
```
(Enter your password when prompted.)

If successful, you should see:
```
etl_project=#
```
💪 **Now PostgreSQL is ready for your ETL pipeline!**  

---

## 📌 6️⃣ Run SQL Scripts (Optional)
To execute SQL files from the `sql/` directory in PowerShell:
```powershell
psql -U myuser -d etl_project -f "C:/Users/your_username/etl-csv-to-sql/sql/analysis_queries.sql"
```

---

## 🚀 Next Steps
- Ensure you have **Python installed** (`python --version`).
- Run the ETL scripts:
  ```powershell
  python scripts/extract_data.py
  python scripts/transform_data.py
  python scripts/load_data.py
  ```
- Check your database for loaded data:
  ```sql
  SELECT * FROM movies LIMIT 5;
  ```

🎉 **PostgreSQL is now fully configured for your ETL project using PowerShell!**

