# mangaeden2kindle
This repository contain a little project, that you can use to send,
via cli tools, a chapter from Manga Eden to your kindle device.

At the moment you need a less secure app password for Gmail (your credentials can be stored in your system's keyring).

#### Installation
* Download [kindlegen](https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000765211) to make MOBI files that can be sent to your devices
* My suggestion is to download the repo and run this (tested with python 3.6.7)
```
pip install -r requirements.txt .
```
* In your home you can make a directory .mangaeden2kindle and the file config.json (see config.json.sample).
If you don't do that, the directory will create at the first run.

#### Usage
```
Usage: m2k [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  get-email             Show the email address from config.json
  get-kindle            Show the kindle address from config.json
  get-list              Show the manga list from mangaeden formatted as title, code  
  send <code> <number-of-chapter>  Send the chapter of manga with code taked from the list
  set-email <email>     Set a new personal email
  set-kindle <email>    Set a new device email
 ```
 
 #### Credits
 This project heavily depends on [KCC (a.k.a. Kindle Comic Converter)](https://github.com/ciromattia/kcc)
