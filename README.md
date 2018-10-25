<div align="center">
<h3>PYTODO</h3>
<img src="https://github.com/aesophor/py-todo/raw/master/assets/scrot.png">

</div>

## Overview
A little program to remind you of upcoming events / unfinished tasks.

Put them into `~/.zshrc` or `~/.bashrc` or whatever you want, and it will stop you from
putting off important shit.

Pickled (i.e., serialized) todo list objects are saved in ~/.local/share/py-todo/todo.dat by default.

## Dependencies
* Linux
* OSX (tested on 10.14 Mojave)
* python 3.6 (pathlib, pickle)

## Installation
Currently it only supports manual installation, sorry!
* Manual Installation (Linux)
```
$ git clone https://github.com/aesophor/py-todo.git
$ cd py-todo && cp todo ~/.local/bin/todo
```
* Manual Installation (OSX)
```
$ git clone https://github.com/aesophor/py-todo.git
$ cd py-todo && cp todo /usr/local/bin/
```

## Usage
```
$ todo                        # List all items.
$ todo -a                     # Add an item.
$ todo -r <index>             # Remove an existing item.
$ todo -h                     # Display help message.
$ todo -v                     # Display version info.
$ todo -org <filename>        # Adds TODOs from Emacs org mode
```

## License
Available under the [MIT License](https://github.com/aesophor/dotfiles/blob/master/LICENSE).
