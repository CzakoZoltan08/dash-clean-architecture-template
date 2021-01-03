from app import app, server

from routes import render_page_content

from layout.sidebar.sidebar_callbacks import toggle_collapse, toggle_classname
from settings import APP_HOST, APP_PORT, APP_DEBUG


if __name__ == "__main__":
    print(APP_HOST)
    app.run_server(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG)