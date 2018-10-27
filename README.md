
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
* python 3.6 (pathlib, pickle)

## Supported Platforms
* Linux
* OSX (tested on 10.14 Mojave)

## Installation
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
$ todo -e <index>                        # Edits an item. (with Title / Expiry Date prompt)
$ todo -e <index> <titls> <expiry_date>  # Edits an item. (without Title / Expiry Date prompt)
$ todo -r <indices>                      # Remove one or more items.
$ todo -h                                # Display help message.
$ todo -v                                # Display version info.
$ todo -org <filename>                     # Adds TODOs from Emacs org mode
```

## Configuration
This part is totally optional. Edit ~/.config/py-todo/config:
```
detail_mode = true / false
week_start_day = Sun / Mon
color = true / false
```

With **detail_mode** set to **true**:
```
Discrete Mathematics Exam (Next Wednesday; 5 days left)
```

With **detail_mode** set to **false**:
```
Discrete Mathematics Exam (5 days left)
```

## License
Available under the [MIT License](https://github.com/aesophor/py-todo/blob/master/LICENSE)
