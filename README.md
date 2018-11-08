
<div align="center">
<h3>PY-TODO</h3>
<img src="https://github.com/aesophor/py-todo/raw/master/assets/scrot.png">

</div>

## Overview
A little program to remind you of upcoming events / unfinished tasks.

Put them into `~/.zshrc` or `~/.bashrc` or whatever you want, and it will stop you from
putting off important shit.

Pickled (i.e., serialized) todo list objects are saved in ~/.local/share/py-todo/todo.dat by default.


## Dependencies
* python >=3.5 (sys, re, pickle, pathlib, datetime)

## Supported Platforms
* Linux
* OSX (tested on 10.14 Mojave)

## Installation
* Debian / Ubuntu / Mint
```
# Download .deb from the release page (https://github.com/aesophor/py-todo/releases)
sudo dpkg -i py-todo_1.3.3-3_all.deb
```

* Arch Linux - [AUR](https://aur.archlinux.org/packages/py-todo) (Submitted by [RewoundVHS](https://github.com/RewoundVHS))
```
yay -S py-todo
```

* Manual Installation (Linux)
```
$ git clone https://github.com/aesophor/py-todo.git
$ cd py-todo && sudo cp todo /usr/bin/todo
```

* Manual Installation (OSX)
```
$ git clone https://github.com/aesophor/py-todo.git
$ cd py-todo && cp todo /usr/local/bin/
```

## Usage
```
$ todo                                   # List all items.
$ todo -a                                # Add an item. (with Title / Expiry Date prompt)
$ todo -a <title> <expiry_date>          # Add an item. (without Title / Expiry Date prompt)
$ todo -e <index>                        # Edit an item. (with Title / Expiry Date prompt)
$ todo -e <index> <title> <expiry_date>  # Edit an item. (without Title / Expiry Date prompt)
$ todo -m --move <index> <new index>     # Move an item from index to new index.
$ todo -r <indices>                      # Remove one or more items.
$ todo -h                                # Display help message.
$ todo -v                                # Display version info.
$ todo -org <filename>                   # Adds TODOs from Emacs org mode
```

## Configuration (Optional)
The default config location is `~/.config/py-todo/config`

```
color = true / false
detail_mode = true / false
```

## Detail Mode
```
Discrete Mathematics Exam (Next Wednesday; 5 days left)  # detail_mode = true
Discrete Mathematics Exam (5 days left)                  # detail_mode = false
```

## Contributors
Special thanks to all the contributors! (In lexicographical order)
* [Arsukeey](https://github.com/Arsukeey) - Added Detail Mode (e.g., Next Wednesday)
* [christophergeiger3](https://github.com/christophergeiger3) - Reformatted code
* [diplozoon](https://github.com/diplozoon) - Reformatted code
* [luvhalvorson](https://github.com/luvhalvorson) - Updated README.md
* [MMarinov97](https://github.com/MMarinov97) - Added compatibility with emacs org file
* [patatman](https://github.com/patatman) - Improved -a --add. Tested py-todo on MacOS
* [RewoundVHS](https://github.com/RewoundVHS) - AUR Package Maintainer, Color Mode
* [Steampunkery](https://github.com/Steampunkery) - Added -e --edit, -m --move, refactoring

## License
Available under the [MIT License](https://github.com/aesophor/py-todo/blob/master/LICENSE)
