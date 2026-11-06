# Quick Start — Smart Document Verification Portal

## ✅ Dependencies Installed Successfully!

All Python packages have been installed. Now complete the database setup.

---

## Next Steps

### Step 1: Configure MySQL Database

1. **Create the database** in MySQL:
   ```sql
   CREATE DATABASE smart_doc_verify CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

2. **Edit the `.env` file**:
   ```powershell
   notepad .env
   ```

   Update these lines with your MySQL password:
   ```env
   SECRET_KEY=<generate-with-command-below>
   DATABASE_URL=mysql+pymysql://root:YOUR_MYSQL_PASSWORD@localhost:3306/smart_doc_verify
   ADMIN_PASSWORD=YourChosenAdminPassword123!
   ```

   Generate a SECRET_KEY:
   ```powershell
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

### Step 2: Run Setup Script

```powershell
powershell -ExecutionPolicy Bypass -File setup.ps1
```

This will:
- ✅ Initialize the database schema
- ✅ Create all tables
- ✅ Seed 10 document categories
- ✅ Create the admin user

### Step 3: Start the Application

```powershell
python run.py
```

### Step 4: Access the Portal

- **Public Portal:** http://127.0.0.1:5000
- **Admin Dashboard:** http://127.0.0.1:5000/admin/login
  - Email: `admin@example.com` (or what you set in .env)
  - Password: (your ADMIN_PASSWORD from .env)

---

## Alternative: Manual Setup

If the setup script doesn't work, run these commands manually:

```powershell
# Set Flask app
$env:FLASK_APP = "run.py"

# Initialize migrations
python -m flask db init

# Create migration
python -m flask db migrate -m "Initial schema"

# Apply to database
python -m flask db upgrade

# Seed data
python -m flask seed-db

# Start app
python run.py
```

---

## Troubleshooting

### MySQL Connection Error
**Error:** `Can't connect to MySQL server`

**Fix:**
1. Ensure MySQL service is running
2. Verify DATABASE_URL in .env
3. Test connection: `mysql -u root -p`

### Tesseract Not Found
**Error:** `TesseractNotFoundError`

**Fix:**
1. Install from: https://github.com/UB-Mannheim/tesseract/wiki
2. Update TESSERACT_CMD in .env if installed elsewhere

### Database Already Exists Error
**Error:** `Can't create database 'smart_doc_verify'; database exists`

**Fix:** Database is already created - skip Step 1, proceed to Step 2

---

## Testing the Application

Once running, test with:

1. Go to http://127.0.0.1:5000/verify/
2. Select "PAN Card" category
3. Create a test text file with:
   ```
   INCOME TAX DEPARTMENT
   Permanent Account Number
   Name: TEST USER
   DOB: 01/01/1990
   ABCDE1234F
   ```
4. Convert to image (PNG/JPG) or save as is
5. Upload and verify

---

**Ready to begin!** Run the setup script above to complete installation.
