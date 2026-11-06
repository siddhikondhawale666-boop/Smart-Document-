"""
Project structure verification script.
Checks that all required files exist and Python files have valid syntax.
"""
import os
import ast
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
REQUIRED_FILES = [
    # Core files
    "run.py",
    "manage.py",
    "requirements.txt",
    "README.md",
    ".env.example",
    ".gitignore",
    
    # App structure
    "app/__init__.py",
    "app/config.py",
    
    # Blueprints
    "app/blueprints/__init__.py",
    "app/blueprints/public.py",
    "app/blueprints/verify.py",
    "app/blueprints/admin.py",
    
    # Models
    "app/models/__init__.py",
    "app/models/admin_user.py",
    "app/models/document_category.py",
    "app/models/verification_record.py",
    
    # Services
    "app/services/__init__.py",
    "app/services/ocr_service.py",
    "app/services/verification_service.py",
    
    # Validators (all 10)
    "app/validators/__init__.py",
    "app/validators/base.py",
    "app/validators/registry.py",
    "app/validators/aadhaar.py",
    "app/validators/pan.py",
    "app/validators/passport.py",
    "app/validators/driving_licence.py",
    "app/validators/voter_id.py",
    "app/validators/vehicle_rc.py",
    "app/validators/birth_certificate.py",
    "app/validators/educational_certificate.py",
    "app/validators/ration_card.py",
    "app/validators/employee_id.py",
    
    # Utils
    "app/utils/__init__.py",
    "app/utils/file_utils.py",
    "app/utils/helpers.py",
    "app/utils/error_handlers.py",
    "app/utils/seed_db.py",
    
    # Static files
    "app/static/css/style.css",
    "app/static/css/admin.css",
    "app/static/js/main.js",
    
    # Templates
    "app/templates/base.html",
    "app/templates/public/home.html",
    "app/templates/public/verify.html",
    "app/templates/public/result.html",
    "app/templates/public/about.html",
    "app/templates/public/privacy.html",
    "app/templates/admin/base_admin.html",
    "app/templates/admin/dashboard.html",
    "app/templates/admin/login.html",
    "app/templates/admin/categories.html",
    "app/templates/admin/category_config.html",
    "app/templates/admin/records.html",
    "app/templates/admin/record_detail.html",
    "app/templates/errors/400.html",
    "app/templates/errors/403.html",
    "app/templates/errors/404.html",
    "app/templates/errors/413.html",
    "app/templates/errors/429.html",
    "app/templates/errors/500.html",
    
    # Tests
    "tests/__init__.py",
    "tests/conftest.py",
    "tests/test_app_startup.py",
    "tests/test_auth.py",
    "tests/test_db.py",
    "tests/test_file_utils.py",
    "tests/test_helpers.py",
    "tests/test_validators.py",
]


def check_file_exists(filepath):
    """Check if a file exists."""
    full_path = PROJECT_ROOT / filepath
    return full_path.exists()


def check_python_syntax(filepath):
    """Check if a Python file has valid syntax."""
    full_path = PROJECT_ROOT / filepath
    if not full_path.suffix == '.py':
        return True, None
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        return True, None
    except SyntaxError as e:
        return False, str(e)


def main():
    print("=" * 70)
    print("SMART DOCUMENT VERIFICATION PORTAL — PROJECT STRUCTURE VERIFICATION")
    print("=" * 70)
    print()
    
    # Check file existence
    print("📁 Checking required files...")
    missing_files = []
    for filepath in REQUIRED_FILES:
        exists = check_file_exists(filepath)
        if exists:
            print(f"  ✓ {filepath}")
        else:
            print(f"  ✗ {filepath} — MISSING")
            missing_files.append(filepath)
    
    print()
    if missing_files:
        print(f"❌ {len(missing_files)} files are missing!")
        return 1
    else:
        print(f"✅ All {len(REQUIRED_FILES)} required files exist!")
    
    print()
    print("🐍 Checking Python syntax...")
    
    python_files = [f for f in REQUIRED_FILES if f.endswith('.py')]
    syntax_errors = []
    
    for filepath in python_files:
        valid, error = check_python_syntax(filepath)
        if valid:
            print(f"  ✓ {filepath}")
        else:
            print(f"  ✗ {filepath} — SYNTAX ERROR: {error}")
            syntax_errors.append((filepath, error))
    
    print()
    if syntax_errors:
        print(f"❌ {len(syntax_errors)} Python files have syntax errors!")
        return 1
    else:
        print(f"✅ All {len(python_files)} Python files have valid syntax!")
    
    # Check directories
    print()
    print("📂 Checking directories...")
    required_dirs = [
        "app", "app/blueprints", "app/models", "app/services",
        "app/validators", "app/utils", "app/static", "app/static/css",
        "app/static/js", "app/static/images", "app/templates",
        "app/templates/public", "app/templates/admin", "app/templates/errors",
        "tests", "tests/fixtures", "instance", "temp_uploads", "migrations",
    ]
    
    missing_dirs = []
    for dirpath in required_dirs:
        full_path = PROJECT_ROOT / dirpath
        if full_path.exists():
            print(f"  ✓ {dirpath}/")
        else:
            print(f"  ✗ {dirpath}/ — MISSING")
            missing_dirs.append(dirpath)
    
    print()
    if missing_dirs:
        print(f"⚠️  {len(missing_dirs)} directories are missing (may be created on first run)")
    else:
        print(f"✅ All {len(required_dirs)} directories exist!")
    
    # Summary
    print()
    print("=" * 70)
    print("VERIFICATION SUMMARY")
    print("=" * 70)
    print(f"Files checked:     {len(REQUIRED_FILES)}")
    print(f"Python files:      {len(python_files)}")
    print(f"Directories:       {len(required_dirs)}")
    print()
    
    if not missing_files and not syntax_errors:
        print("✅ PROJECT STRUCTURE IS VALID!")
        print()
        print("Next steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Configure .env file with your MySQL credentials")
        print("3. Run database migrations: flask db upgrade")
        print("4. Seed the database: flask seed-db")
        print("5. Start the application: python run.py")
        print()
        return 0
    else:
        print("❌ PROJECT STRUCTURE HAS ISSUES!")
        print()
        if missing_files:
            print(f"Missing files: {len(missing_files)}")
        if syntax_errors:
            print(f"Syntax errors: {len(syntax_errors)}")
        print()
        return 1


if __name__ == "__main__":
    sys.exit(main())
