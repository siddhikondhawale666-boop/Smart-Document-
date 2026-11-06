# Smart Document Verification Portal - Setup Script
# Run this script to complete the database setup

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Smart Document Verification Portal - Database Setup" -ForegroundColor Cyan
Write-Host "============================================================`n" -ForegroundColor Cyan

# Set Flask app
$env:FLASK_APP = "run.py"

# Step 1: Check if .env exists
if (!(Test-Path ".env")) {
    Write-Host "[1/5] Creating .env file from template..." -ForegroundColor Yellow
    Copy-Item ".env.example" ".env"
    Write-Host "      ✓ .env file created" -ForegroundColor Green
    Write-Host "      ⚠ IMPORTANT: Edit .env and configure your MySQL password!" -ForegroundColor Red
    Write-Host "      Press any key to continue after editing .env..." -ForegroundColor Yellow
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
} else {
    Write-Host "[1/5] .env file already exists" -ForegroundColor Green
}

# Step 2: Test database connection
Write-Host "`n[2/5] Testing database connection..." -ForegroundColor Yellow
try {
    python -c "from app import create_app; app = create_app('development'); print('✓ Database connection successful')" 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "      ✓ Database connection successful" -ForegroundColor Green
    } else {
        Write-Host "      ✗ Database connection failed!" -ForegroundColor Red
        Write-Host "      Please ensure:" -ForegroundColor Yellow
        Write-Host "        1. MySQL is running" -ForegroundColor Yellow
        Write-Host "        2. Database 'smart_doc_verify' exists" -ForegroundColor Yellow
        Write-Host "        3. Credentials in .env are correct" -ForegroundColor Yellow
        Write-Host "`n      To create database, run in MySQL:" -ForegroundColor Yellow
        Write-Host "        CREATE DATABASE smart_doc_verify CHARACTER SET utf8mb4;" -ForegroundColor White
        exit 1
    }
} catch {
    Write-Host "      ⚠ Could not test connection (this is OK if database doesn't exist yet)" -ForegroundColor Yellow
}

# Step 3: Run migrations
Write-Host "`n[3/5] Creating database migration..." -ForegroundColor Yellow
python -m flask db migrate -m "Initial schema" 2>&1 | Out-String | ForEach-Object {
    if ($_ -match "ERROR") {
        Write-Host "      ✗ Migration failed: $_" -ForegroundColor Red
        Write-Host "`n      Common fixes:" -ForegroundColor Yellow
        Write-Host "        - Ensure MySQL database exists: CREATE DATABASE smart_doc_verify;" -ForegroundColor White
        Write-Host "        - Check DATABASE_URL in .env file" -ForegroundColor White
        Write-Host "        - Verify MySQL is running" -ForegroundColor White
        exit 1
    }
}
if ($LASTEXITCODE -eq 0) {
    Write-Host "      ✓ Migration created" -ForegroundColor Green
}

# Step 4: Apply migrations
Write-Host "`n[4/5] Applying migrations to database..." -ForegroundColor Yellow
python -m flask db upgrade 2>&1 | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "      ✓ Database schema created" -ForegroundColor Green
} else {
    Write-Host "      ✗ Migration failed!" -ForegroundColor Red
    exit 1
}

# Step 5: Seed database
Write-Host "`n[5/5] Seeding database with categories and admin user..." -ForegroundColor Yellow
python -m flask seed-db 2>&1 | Out-Null
if ($LASTEXITCODE -eq 0) {
    Write-Host "      ✓ Database seeded" -ForegroundColor Green
} else {
    Write-Host "      ✗ Seeding failed!" -ForegroundColor Red
    exit 1
}

# Success message
Write-Host "`n============================================================" -ForegroundColor Green
Write-Host "✓ Setup Complete!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host "`nYou can now start the application with:" -ForegroundColor Cyan
Write-Host "  python run.py`n" -ForegroundColor White
Write-Host "Access the portal at:" -ForegroundColor Cyan
Write-Host "  http://127.0.0.1:5000" -ForegroundColor White
Write-Host "`nAdmin login:" -ForegroundColor Cyan
Write-Host "  http://127.0.0.1:5000/admin/login" -ForegroundColor White
Write-Host "  Email: admin@example.com (or what you set in .env)" -ForegroundColor Yellow
Write-Host "  Password: (ADMIN_PASSWORD from .env)`n" -ForegroundColor Yellow
