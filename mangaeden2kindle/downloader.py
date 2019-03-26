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

from PIL import Image
import requests
from io import BytesIO
from . import mangaeden_api, util


def open_img(cdn_path):
    response = requests.get(f"{util.CDN_URL}/{cdn_path}")
    return Image.open(BytesIO(response.content))


def download_chapter(code, number):
    chap_dir = util.DATA_DIR / code / str(number)
    util.make_dir(chap_dir)
    try:
        images = mangaeden_api.get_chapter_images(code, number)
        for im in images:
            open_img(im[1]).convert("RGB").save((chap_dir / str(im[0])).with_suffix('.jpeg'), 'jpeg')
    except Exception as e:
        print(e.with_traceback())
        util.delete_dir(chap_dir)
        raise e
