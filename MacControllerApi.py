import threading
from src import MacControllerTray


def start_api(win: MacControllerTray):
    print("Flask App Initializing...")
    win.flask_app.run('0.0.0.0', 5888, debug=False, use_reloader=False)


if __name__ == "__main__":
    win = MacControllerTray("MacController")
    flask_thread = threading.Thread(target=start_api, args=(win,))
    flask_thread.start()
    win.run()
