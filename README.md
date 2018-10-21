<div align="center">
<h3>PYTODO</h3>
<img src="https://github.com/aesophor/py-todo/raw/master/assets/scrot.png">

</div>

## Overview
A little program to remind you of upcoming events / unfinished tasks.

## Dependencies
* python 3.6 (pathlib, pickle)

## Installation
Currently it only supports manual installation, sorry! 
* Manual Installation
```
$ git clone https://github.com/aesophor/py-todo.git
$ cd py-todo && cp todo ~/.local/bin/todo
```

Todo list items are saved in ~/.local/share/py-todo/todo.dat by default.

## Usage
```
$ todo                        # List all items.
$ todo -a                     # Add an item.
$ todo -r <index>             # Remove an existing item.
$ todo -h                     # Display help message.
$ todo -v                     # Display version info.
```

## License
Available under the [MIT License](https://github.com/aesophor/dotfiles/blob/master/LICENSE).
