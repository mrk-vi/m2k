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

import os

from . import downloader, util


def make_chapter_book(code, number):
    try:
        if number > 0:
            downloader.download_chapter(code, number)
        os.system(f"kcc-c2e -p KPW -f MOBI -m {util.DATA_DIR / code / str(number)}")
    except Exception as e:
        print(e)
        raise FileNotFoundError
    return (util.DATA_DIR / code / str(number)).with_suffix(".mobi")


def make_manga_book(code, from_, to_):
    if to_ > from_ > 0:
        for i in range(from_, to_+1):
            downloader.download_chapter(code, i)
    os.system(f"kcc-c2e -p KPW -f MOBI -m {util.DATA_DIR/code}")


def send_chapter_book(code, number):
    try:
        book_path = str(make_chapter_book(code, number))
        util.send_email(book_path)
    except Exception as err:
        print(err)

