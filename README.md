# Smart Document Verification Portal

A full-stack document verification system that uses OCR (Optical Character Recognition) and rule-based validation to automatically verify the format of 10 common Indian identity and official documents.

## 🎯 Project Overview

This college field project demonstrates automated document verification using:
- **Tesseract OCR** for text extraction from images and PDFs
- **Category-specific validation rules** based on documented format standards
- **Flask web framework** with a modern, responsive UI
- **MySQL database** with SQLAlchemy ORM for record tracking
- **Admin dashboard** for analytics and management

**Important:** This system performs **format validation only**. It does not connect to any government database and cannot confirm document authenticity.

## 📋 Supported Documents

1. **Aadhaar Card** — 12-digit UIDAI number with Verhoeff check digit
2. **PAN Card** — 10-character Income Tax number with taxpayer type validation
3. **Indian Passport** — Passport number format, issue/expiry date checks
4. **Driving Licence** — State-RTO-Year-Serial format validation
5. **Voter ID** — EPIC number (3 letters + 7 digits)
6. **Vehicle Registration Certificate** — Registration number format
7. **Birth Certificate** — Required field and date validation
8. **Educational Certificate** — Institution, qualification, year checks
9. **Ration Card** — Card category and holder information
10. **Employee ID Card** — Organization-specific configurable rules

## 🛠️ Technology Stack

### Backend
- **Python 3.11+**
- **Flask 3.0** — Web framework
- **Flask-SQLAlchemy** — ORM
- **Flask-Migrate** — Database migrations
- **Flask-Login** — Authentication
- **Flask-WTF** — CSRF protection
- **Flask-Limiter** — Rate limiting

### OCR & Image Processing
- **Tesseract OCR** (pytesseract) — Text extraction
- **Pillow (PIL)** — Image preprocessing
- **OpenCV** — Advanced image enhancement
- **PyMuPDF** — PDF processing

### Database
- **MySQL 8.0+** with PyMySQL connector
- SQLAlchemy models with proper relationships and migrations

### Frontend
- **HTML5, CSS3, JavaScript**
- **Font Awesome 6** icons
- **Chart.js** for admin analytics
- Responsive design (desktop, tablet, mobile)

## 📁 Project Structure

```
Smart Document/
├── app/
│   ├── __init__.py              # Application factory
│   ├── config.py                # Configuration classes
│   ├── blueprints/              # Route blueprints
│   │   ├── public.py            # Home, about, privacy
│   │   ├── verify.py            # Document verification
│   │   └── admin.py             # Admin dashboard
│   ├── models/                  # Database models
│   │   ├── admin_user.py
│   │   ├── document_category.py
│   │   └── verification_record.py
│   ├── services/                # Business logic
│   │   ├── ocr_service.py       # OCR pipeline
│   │   └── verification_service.py
│   ├── validators/              # Document validators
│   │   ├── base.py              # Base structures
│   │   ├── registry.py          # Validator registry
│   │   ├── aadhaar.py
│   │   ├── pan.py
│   │   ├── passport.py
│   │   └── ... (7 more)
│   ├── utils/                   # Utilities
│   │   ├── file_utils.py        # Upload handling
│   │   ├── helpers.py           # General helpers
│   │   ├── error_handlers.py
│   │   └── seed_db.py           # Database seeding
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── admin.css
│   │   └── js/
│   │       └── main.js
│   └── templates/
│       ├── base.html
│       ├── public/              # Public pages
│       ├── admin/               # Admin pages
│       └── errors/              # Error pages
├── tests/                       # Automated tests
├── migrations/                  # Database migrations
├── instance/                    # Instance-specific files
├── temp_uploads/                # Temporary upload folder
├── requirements.txt
├── run.py                       # Application entry point
├── manage.py                    # CLI commands
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites

1. **Python 3.11 or higher**
   ```powershell
   python --version
   ```

2. **MySQL 8.0 or higher**
   - Install MySQL Server from https://dev.mysql.com/downloads/installer/
   - Remember your root password during installation

3. **Tesseract OCR**
   - Download Windows installer: https://github.com/UB-Mannheim/tesseract/wiki
   - Install to default location: `C:\Program Files\Tesseract-OCR`
   - Add to PATH if prompted

### Step 1: Clone or Extract Project

```powershell
cd "e:\Smart Document"
```

### Step 2: Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Python Dependencies

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

This installs Flask, SQLAlchemy, pytesseract, Pillow, OpenCV, PyMuPDF, and all other dependencies.

### Step 4: Configure MySQL Database

1. Open MySQL Command Line Client or MySQL Workbench

2. Create the database:
   ```sql
   CREATE DATABASE smart_doc_verify CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. Create a database user (optional but recommended):
   ```sql
   CREATE USER 'docverify'@'localhost' IDENTIFIED BY 'YourSecurePassword123';
   GRANT ALL PRIVILEGES ON smart_doc_verify.* TO 'docverify'@'localhost';
   FLUSH PRIVILEGES;
   ```

### Step 5: Configure Environment Variables

1. Copy the example environment file:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Edit `.env` and update:

   ```env
   SECRET_KEY=your-very-secret-key-change-this
   FLASK_ENV=development
   FLASK_DEBUG=1

   # MySQL connection (update with your credentials)
   DATABASE_URL=mysql+pymysql://root:YourMySQLPassword@localhost:3306/smart_doc_verify

   # Tesseract path (verify this matches your installation)
   TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe

   # Admin account (used for initial seeding)
   ADMIN_EMAIL=admin@example.com
   ADMIN_PASSWORD=ChangeThisAdminPassword123!

   ENABLE_RECORD_RETENTION=1
   MAX_CONTENT_LENGTH_MB=10
   RATE_LIMIT_PER_MINUTE=10
   ```

   Generate a secure SECRET_KEY:
   ```powershell
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

### Step 6: Initialize Database

```powershell
# Create migration repository (first time only)
flask db init

# Generate initial migration
flask db migrate -m "Initial schema"

# Apply migrations to database
flask db upgrade

# Seed categories and admin user
flask seed-db
```

### Step 7: Verify Tesseract Installation

```powershell
& "C:\Program Files\Tesseract-OCR\tesseract.exe" --version
```

You should see Tesseract version information. If not, reinstall Tesseract or update the path in `.env`.

### Step 8: Run the Application

```powershell
python run.py
```

The application will start at: **http://127.0.0.1:5000**

## 🧪 Running Tests

The project includes automated tests using pytest.

```powershell
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_validators.py

# Run with coverage report
pytest --cov=app --cov-report=html
```

## 📖 Usage Guide

### For Users (Public Portal)

1. **Visit the home page** at http://127.0.0.1:5000
2. **Click "Verify a Document"**
3. **Select a document category** from the 10 options
4. **Upload your document** (PNG, JPG, TIFF, BMP, or PDF — max 10 MB)
5. **Click "Verify Document"**
6. **View the detailed report** with:
   - Format validation results
   - Extracted fields (sensitive values masked)
   - Individual check pass/fail status
   - Expiry information (where applicable)
   - Authenticity disclaimer

### For Administrators

1. **Login** at http://127.0.0.1:5000/admin/login
   - Default email: `admin@example.com`
   - Default password: (the one you set in `.env`)

2. **Dashboard** — View statistics and trends
3. **Records** — Search and filter verification history
4. **Categories** — Enable/disable document types, configure validation rules

### Creating Additional Admin Users

```powershell
flask create-admin
```

Follow the prompts to create a new admin account.

## 🔧 Configuration

### Upload Settings

Edit `.env`:
```env
MAX_CONTENT_LENGTH_MB=10         # Maximum file size
TEMP_UPLOAD_FOLDER=temp_uploads  # Temporary storage folder
```

### Rate Limiting

```env
RATE_LIMIT_PER_MINUTE=10  # Verification requests per minute per IP
```

### Record Retention

```env
ENABLE_RECORD_RETENTION=1  # 1=enabled, 0=disabled
```

When disabled, verification reports are displayed but not saved to the database.

### Document Category Configuration

Admins can configure validation rules per category via the admin panel:

1. Go to **Admin > Categories**
2. Click **Config** for a category
3. Edit the JSON configuration

Example (Employee ID):
```json
{
  "required_keywords": ["COMPANY NAME", "DEPARTMENT"]
}
```

## 🔒 Security & Privacy

### What is Protected

- ✅ CSRF protection on all forms
- ✅ Password hashing with Werkzeug
- ✅ Secure session configuration
- ✅ File type validation (extension + magic bytes)
- ✅ File size limits enforced
- ✅ Rate limiting on verification endpoint
- ✅ Uploaded files deleted after processing
- ✅ Sensitive identity numbers masked in reports and database
- ✅ Admin authentication required for dashboard
- ✅ SQL injection prevention via ORM parameterization

### What is Stored (When Retention is Enabled)

- Verification reference ID
- Document category
- Timestamp
- Format validation result (passed/failed/partial/unreadable)
- Check counts (passed, failed, warning, unable)
- Sanitised extracted metadata (e.g., masked numbers)
- Summary and notes

### What is NEVER Stored

- Original uploaded files
- Full identity numbers (Aadhaar, PAN, etc.)
- Raw OCR output text
- User IP addresses or personal info (unless logged by web server)

## ⚠️ Important Limitations

1. **Format Validation Only**
   - This system checks if a document matches expected format rules
   - It does NOT verify with UIDAI, NSDL, Parivahan, or any government API
   - A "passed" result does not mean the document is genuine

2. **OCR Accuracy**
   - Depends on image quality, resolution, lighting, and clarity
   - Blurry, low-resolution, or rotated documents may fail
   - Character confusion (O/0, I/1, S/5, B/8) can affect validation

3. **Educational Use**
   - This is a college demonstration project
   - Not suitable for production use without additional verification mechanisms

4. **No Authenticity Guarantee**
   - Format checks cannot detect forgery, tampering, or fake documents
   - Official verification requires government-issued APIs and authorization

## 🐛 Troubleshooting

### MySQL Connection Error

**Error:** `Can't connect to MySQL server`

**Solution:**
- Ensure MySQL service is running: `services.msc` → find MySQL → Start
- Verify credentials in `.env` match your MySQL setup
- Test connection: `mysql -u root -p` in Command Prompt

### Tesseract Not Found

**Error:** `TesseractNotFoundError`

**Solution:**
- Verify installation: `& "C:\Program Files\Tesseract-OCR\tesseract.exe" --version`
- Update `TESSERACT_CMD` path in `.env` if installed elsewhere
- Reinstall from https://github.com/UB-Mannheim/tesseract/wiki

### Flask Migrations Error

**Error:** `Target database is not up to date`

**Solution:**
```powershell
flask db upgrade
```

### Import Errors

**Error:** `ModuleNotFoundError: No module named 'app'`

**Solution:**
- Ensure virtual environment is activated: `.\venv\Scripts\Activate.ps1`
- Reinstall dependencies: `pip install -r requirements.txt`

### Port Already in Use

**Error:** `Address already in use`

**Solution:**
- Change port in `run.py`: `app.run(port=5001)`
- Or stop the process using port 5000

### Image Upload Fails

**Error:** File validation fails despite correct format

**Solution:**
- Check file size (must be under 10 MB)
- Ensure file is not corrupted
- Try a different image format (PNG or PDF recommended)

## 📚 Validation Rules Reference

### Aadhaar Card
- 12 digits (grouped as 4-4-4)
- First digit must not be 0 or 1
- Verhoeff check digit validation
- Name, DOB, and gender field detection

### PAN Card
- Format: 5 letters + 4 digits + 1 letter
- 4th character indicates taxpayer type (P=Individual, C=Company, etc.)
- Income Tax Department keyword check

### Indian Passport
- Format: 1 letter + 7 digits
- Issue and expiry date parsing
- Expiry status check
- Nationality field detection

### Driving Licence
- Format: SS-RR-YYYY-NNNNNNN (State-RTO-Year-Serial)
- Valid state codes
- Issue and expiry date validation

### Voter ID (EPIC)
- Format: 3 letters + 7 digits
- Election Commission keyword check

### Vehicle RC
- Registration format: SS99AA9999 or SS99A9999
- RTO keyword detection
- Fitness validity check

### Birth Certificate
- Date of birth validation (not in future)
- Required fields: child name, parent names, issuing authority

### Educational Certificate
- Institution/university name required
- Qualification detection (degree/diploma type)
- Year plausibility (1950–current)

### Ration Card
- Card category (APL/BPL/AAY)
- Holder name and issuing authority

### Employee ID
- Employee ID number and name required
- Organization-specific configurable keywords
- Validity date check

## 🎓 Project Report Sections

This project satisfies typical college field project requirements:

- **Problem Statement:** Manual document verification is slow and error-prone
- **Objectives:** Automate format checking using OCR and validation rules
- **Scope:** 10 Indian document categories with dedicated validators
- **Methodology:** OCR → text normalization → regex validation → report generation
- **Results:** Functional web application with admin dashboard and analytics
- **Limitations:** Format checks only; no government API integration
- **Future Enhancements:** ML-based fraud detection, blockchain verification records, mobile app

## 📄 License

This is a college field project for educational purposes. Not licensed for commercial use.

## 👨‍💻 Developer

Third-year B.Sc. Computer Science student  
College Field Project — Smart Document Verification Portal

## 🙏 Acknowledgments

- **Tesseract OCR** — Google's open-source OCR engine
- **Flask** — Lightweight Python web framework
- **Font Awesome** — Icon library
- **Chart.js** — JavaScript charting library
- College faculty and project guide for their support

---

## Quick Start Checklist

- [ ] Python 3.11+ installed
- [ ] MySQL 8.0+ installed and running
- [ ] Tesseract OCR installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file configured with database credentials
- [ ] Database created in MySQL
- [ ] Migrations applied (`flask db upgrade`)
- [ ] Database seeded (`flask seed-db`)
- [ ] Application running (`python run.py`)
- [ ] Tested with a sample document upload

**Access Points:**
- **Public Portal:** http://127.0.0.1:5000
- **Admin Login:** http://127.0.0.1:5000/admin/login

For questions or issues, refer to the Troubleshooting section above.
