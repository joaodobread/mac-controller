from src.api.qr_code import open_qr_code
from src.api import init_app
import rumps


class MacControllerTray(rumps.App):
    def __init__(self, name, title=None, icon=None, template=None, menu=None, quit_button='Quit'):
        super().__init__(name, title, 'images/pony.jpg', template, menu, quit_button)
        self.flask_app = init_app()

    def start_api(self):
        self.flask_app.run('0.0.0.0', 5888, debug=False, use_reloader=False)

    @rumps.clicked('QrCode')
    def qr_code(self, _):
        open_qr_code()
