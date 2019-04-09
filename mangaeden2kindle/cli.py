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

import click

from mangaeden2kindle import kindle, util, config


@click.group()
def main():
    pass


@main.command()
def get_list():
    click.echo(util.formatted_list())


@main.command()
@click.argument('name')
@click.argument('number', type=int)
def send(name, number):
    kindle.send_chapter_book(name, number)


@main.command()
@click.argument('email')
def set_kindle(email):
    util.set_kindle_address(email)


@main.command()
@click.argument('email')
def set_email(email):
    util.set_email_address(email)


@main.command()
def get_kindle():
    click.echo(config.kindle_address)


@main.command()
def get_email():
    click.echo(config.email_address)

