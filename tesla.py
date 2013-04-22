import requests
from bs4 import BeautifulSoup


class TeslaMotors:

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password
        self.s = requests.Session()
        self.headers = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31"

        }
        self.s.headers.update(self.headers)
        self.login_url = "https://www.teslamotors.com/user/login"
        self.logged_in = False

    def login(self):

        if not self.username and not self.password:
            raise Exception("Username or password invalid")

        # get the login page for form build id
        r = self.s.get(self.login_url)
        soup = BeautifulSoup(r.content)
        form_build_id = soup.select('input[name=form_build_id]')[0]['value']

        data = {
            'register-url': '/user/register',
            'name': self.username,
            'pass': self.password,
            'form_build_id': form_build_id,
            'form_id': 'user_login',
            'persistent_login': 1,
            'keep_signed_in': 1

        }
        # Authenticate
        self.s.post(self.login_url, data=data, allow_redirects=True, verify=False)

        # TODO add verification of successful login
        self.logged_in = True

    def get_page(self, url):
        if not self.logged_in:
            self.login()

        return self.s.get(url)


