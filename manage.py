"""
Flask CLI management commands.
Usage:
  flask seed-db       — populate categories and default admin
  flask create-admin  — create/update admin account interactively
"""
import os
import click
from flask.cli import with_appcontext
from app import create_app, db

app = create_app(os.environ.get("FLASK_ENV", "development"))


@app.cli.command("seed-db")
@with_appcontext
def seed_db():
    """Seed document categories and default admin user."""
    from app.utils.seed_db import seed_categories, seed_admin
    click.echo("Seeding document categories...")
    n = seed_categories()
    click.echo(f"  Added {n} categories.")
    click.echo("Seeding admin user...")
    created = seed_admin()
    if created:
        click.echo(f"  Admin user created: {os.environ.get('ADMIN_EMAIL')}")
    else:
        click.echo("  Admin user already exists or ADMIN_PASSWORD not set.")
    click.echo("Done.")


@app.cli.command("create-admin")
@click.option("--email", prompt="Admin email")
@click.option("--password", prompt="Admin password", hide_input=True, confirmation_prompt=True)
@click.option("--name", default="Administrator", prompt="Display name")
@with_appcontext
def create_admin(email, password, name):
    """Create or update an admin user account."""
    from app.models import AdminUser
    email = email.strip().lower()
    user = AdminUser.query.filter_by(email=email).first()
    if user:
        user.set_password(password)
        user.display_name = name
        db.session.commit()
        click.echo(f"Updated admin user: {email}")
    else:
        user = AdminUser(email=email, display_name=name)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        click.echo(f"Created admin user: {email}")


if __name__ == "__main__":
    app.run()
