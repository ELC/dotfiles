# Symlinks
from homely.files import symlink

from homely.system import execute

# Home Directory

dotfiles = {
    '.bashrc': '.bashrc',
    '.zshrc': '.zshrc',
    '.Xresources': '.Xresources',
    '.vimrc': '.vimrc',

    # I3

    '.config/i3/config': '.config/i3/config',
    '.config/i3/i3blocks.conf': '.config/i3/i3blocks.conf',
    '.config/i3/lock.sh': '.config/i3/lock.sh',
    '.config/i3/toggletouchpad.sh': '.config/i3/toggletouchpad.sh',
    '.config/i3/icon.png': '.config/i3/icon.png',
}

for source, target in dotfiles.items():

    execute(['rm', '-f', source])

    symlink(source, target)


# Oh My ZSH
execute(['rsync', '-a', 'dotfiles/.oh-my-zsh/', '.oh-my-zsh/'])


# Installing Packages
from homely.install import installpkg

# Packages

packages = ['ack', 'feh', 'alsa-utils', 'pulseaudio', 'rofi', 'i3',
            'i3blocks', 'scrot', 'compton', 'zsh', 'wget', 'git',
            'xbacklight', 'vlc', 'pavucontrol', 'numlockx', 'vim',
            'tree',
           ]

for package in packages:
    installpkg(package)

# Fonts

fonts = ['fonts-firacode', 'fonts-font-awesome', 
         'ttf-ancient-fonts', 'fonts-powerline',
        ]

for font in fonts:
    installpkg(font)


