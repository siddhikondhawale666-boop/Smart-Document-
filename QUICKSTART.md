# Quick Start Guide — Smart Document Verification Portal

## Prerequisites Checklist

Before starting, ensure you have:

- [ ] **Python 3.11+** installed (check: `python --version`)
- [ ] **MySQL 8.0+** installed and running
- [ ] **Tesseract OCR** installed at `C:\Program Files\Tesseract-OCR\`
- [ ] **Git Bash or PowerShell** (PowerShell recommended on Windows)

---

## 5-Minute Setup

### Step 1: Install Python Dependencies (2 minutes)

```powershell
# Navigate to project directory
cd "e:\Smart Document"

# Create virtual environment (optional but recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install all dependencies
pip install -r requirements.txt
```

### Step 2: Create MySQL Database (1 minute)

Open MySQL Command Line or MySQL Workbench and run:

```sql
CREATE DATABASE smart_doc_verify CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### Step 3: Configure Environment (1 minute)

```powershell
# Copy environment template
Copy-Item .env.example .env

# Edit .env file with your MySQL password
notepad .env
```

**Update these lines in .env:**
```env
SECRET_KEY=paste-result-from-next-command-here
DATABASE_URL=mysql+pymysql://root:YOUR_MYSQL_PASSWORD@localhost:3306/smart_doc_verify
ADMIN_PASSWORD=ChooseYourAdminPassword123!
```

**Generate SECRET_KEY:**
```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

### Step 4: Initialize Database (1 minute)

```powershell
# Initialize migration system
flask db init

# Create initial migration
flask db migrate -m "Initial database schema"

# Apply migrations to database
flask db upgrade

# Seed categories and admin user
flask seed-db
```

### Step 5: Start Application (10 seconds)

```powershell
python run.py
```

**Application will start at:** http://127.0.0.1:5000

---

## First-Time Access

### Public Portal
- **URL:** http://127.0.0.1:5000
- **Action:** Click "Verify a Document" and test with a sample document

### Admin Dashboard
- **URL:** http://127.0.0.1:5000/admin/login
- **Email:** admin@example.com (or what you set in .env)
- **Password:** (what you set as ADMIN_PASSWORD in .env)

---

## Testing the Application

### Option 1: Upload a Real Document (if you have one)
1. Go to http://127.0.0.1:5000/verify/
2. Select document category (e.g., "PAN Card")
3. Upload your document image or PDF
4. Click "Verify Document"
5. View the report

### Option 2: Create a Test Document
Create a simple text file and save as `test_pan.txt`:
```
INCOME TAX DEPARTMENT
Permanent Account Number Card

Name: TEST USER
Father's Name: PARENT NAME
Date of Birth: 01/04/1990

Permanent Account Number
ABCDE1234F
```

Then:
1. Convert to image using any image editor or online tool
2. Save as PNG or JPG
3. Upload to the verification portal

### Option 3: Run Automated Tests
```powershell
pytest -v
```

---

## Common Issues & Quick Fixes

### Issue: Python not found
**Fix:** Install Python from https://www.python.org/downloads/

### Issue: MySQL connection error
**Fix:** 
1. Ensure MySQL service is running (check Task Manager → Services)
2. Verify password in DATABASE_URL in .env
3. Test connection: `mysql -u root -p`

### Issue: Tesseract not found
**Fix:**
1. Install from: https://github.com/UB-Mannheim/tesseract/wiki
2. Update TESSERACT_CMD path in .env if installed elsewhere

### Issue: Port 5000 already in use
**Fix:** Change port in `run.py`:
```python
app.run(host="0.0.0.0", port=5001)  # Use port 5001 instead
```

### Issue: ModuleNotFoundError
**Fix:**
1. Activate virtual environment: `.\venv\Scripts\Activate.ps1`
2. Reinstall dependencies: `pip install -r requirements.txt`

### Issue: Migration error "Target database is not up to date"
**Fix:**
```powershell
flask db upgrade
```

---

## File Structure Reference

```
Smart Document/
├── run.py                    ← Start the application
├── manage.py                 ← Database management commands
├── requirements.txt          ← Python dependencies
├── .env                      ← Your configuration (NOT in git)
├── .env.example              ← Configuration template
├── README.md                 ← Full documentation
├── QUICKSTART.md             ← This file
│
├── app/                      ← Application code
│   ├── blueprints/           ← Route handlers
│   ├── models/               ← Database models
│   ├── services/             ← Business logic (OCR, verification)
│   ├── validators/           ← 10 document validators
│   ├── utils/                ← Helper functions
│   ├── static/               ← CSS and JS files
│   └── templates/            ← HTML templates
│
├── tests/                    ← Automated tests
├── migrations/               ← Database version control
├── instance/                 ← Instance-specific data
└── temp_uploads/             ← Temporary file processing
```

---

## Command Reference

### Application
```powershell
python run.py                 # Start the application
python verify_structure.py   # Verify project structure
```

### Database
```powershell
flask db migrate -m "msg"    # Create new migration
flask db upgrade             # Apply migrations
flask db downgrade           # Rollback one migration
flask seed-db                # Seed categories and admin
flask create-admin           # Create additional admin user
```

### Testing
```powershell
pytest                       # Run all tests
pytest -v                    # Verbose output
pytest tests/test_db.py      # Run specific test file
pytest --cov=app             # With coverage report
```

### Virtual Environment
```powershell
python -m venv venv          # Create virtual environment
.\venv\Scripts\Activate.ps1  # Activate (Windows PowerShell)
deactivate                   # Deactivate
```

---

## URLs Quick Reference

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:5000 |
| Verify Document | http://127.0.0.1:5000/verify/ |
| About | http://127.0.0.1:5000/about |
| Privacy | http://127.0.0.1:5000/privacy |
| Admin Login | http://127.0.0.1:5000/admin/login |
| Admin Dashboard | http://127.0.0.1:5000/admin/dashboard |
| Admin Records | http://127.0.0.1:5000/admin/records |
| Admin Categories | http://127.0.0.1:5000/admin/categories |

---

## Next Steps After Setup

1. **Test the public portal** — Upload a sample document
2. **Login to admin dashboard** — View verification statistics
3. **Explore category configuration** — Edit validation rules
4. **Review the README.md** — Understand validation rules and architecture
5. **Run automated tests** — Verify everything works
6. **Prepare demo documents** — Create synthetic test files for presentation

---

## Support

For detailed documentation, see **README.md**

For troubleshooting, see the **Troubleshooting** section in README.md

For validation rules reference, see **Validation Rules Reference** in README.md

---

**Setup Time:** ~5 minutes  
**Status:** Ready for college demonstration  
**Documentation:** Complete and verified
