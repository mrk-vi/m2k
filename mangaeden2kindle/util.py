#  MIT License
#
#  Copyright (c) 2019 Mirko Zizzari
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import pathlib
import yagmail
from . import mangaeden_api, config

API_URL = 'https://www.mangaeden.com/api'
CDN_URL = "https://cdn.mangaeden.com/mangasimg"
DATA_DIR = pathlib.Path.cwd()/'data'


def make_dir(path):
    delete_dir(path)
    path.mkdir(parents=True)


def delete_dir(path):
    if path.is_dir():
        for x in (path.glob('*')):
            x.unlink()
        path.rmdir()


def send_email(attach):
    try:
        yag = yagmail.SMTP(config.email_address)
        yag.send(config.kindle_address, 'new chapter', [attach])
    except Exception as e:
        print(e)


def set_kindle_address(email):
    try:
        yagmail.sender.validate_email_with_regex(email)
    except yagmail.error.YagInvalidEmailAddress as e:
        print(e)
    config.set_kindle_address(email)


def set_email_address(email):
    try:
        yagmail.sender.validate_email_with_regex(email)
    except yagmail.error.YagInvalidEmailAddress as e:
        print(e)
    config.set_email_address(email)


def formatted_list():
    for m in mangaeden_api.get_list(1):
        return f"{m['t']}, {m['a']}"

