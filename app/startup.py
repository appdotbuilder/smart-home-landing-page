from app.database import create_tables
from app.landing_service import initialize_default_data
import app.landing_page


def startup() -> None:
    # this function is called before the first request
    create_tables()
    initialize_default_data()
    app.landing_page.create()
