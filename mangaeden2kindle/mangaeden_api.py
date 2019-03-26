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

import requests
from . import util


def get_list(lang):
    """
    Get the list of all mangas on mangaeden

    Parameters:
    lang (int):
        0 for english
        1 for italian
    Returns:
    json encoded : list of the mangas
        example
            a	"one-piece"
            c
                0	"Avventura"
                1	"Azione"
                2	"Shounen"
            h	281219384
            i	"4e70ea94c092255ef7007543"
            im	"b0/b0ac7f12d2cb0fc07b941…0e967396ae70f98d101.png"
            ld	1553329692
            s	1
            t	"One Piece"
    """
    if lang in (0, 1):
        return requests.get(f"{util.API_URL}/list/{lang}").json()['manga']
    else:
        raise ValueError


def get_manga(code, lang=1):
    for i in get_list(lang):
        if i['a'] == code:
            return requests.get(f"{util.API_URL}/manga/{i['i']}").json()


def get_chapters(code):
    return get_manga(code)['chapters']


def get_chapter(code, number):
    chapters = get_chapters(code)
    for c in chapters:
        if c[0] == number:
            chapter_id = c[3]
            return requests.get(f"{util.API_URL}/chapter/{chapter_id}").json()


def get_chapter_images(code, number):
    return get_chapter(code, number)['images']

