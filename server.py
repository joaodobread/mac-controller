from src.api import init_app, run_app


if __name__ == "__main__":
    app = init_app(debug=True, use_reloader=True)
    run_app(app, host='0.0.0.0', port=5888)
