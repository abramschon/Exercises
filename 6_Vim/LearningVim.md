# Learning Vim

Taken from this [tutorial](https://www.linux.com/training-tutorials/vim-101-beginners-guide-vim/)

## Modes

Vim has different modes:
- insert mode
- command mode
- last-line mode

Initially, you are in command mode. To get into insert mode where you can type normally, click `i`. To go out of insert mode, and back into command mode, hit `esc`.

To get into last-line mode, type `:`. From here, you can:
- `w` write the file
- `q` exit the editor

## Navigation

- `h` move the cursor one character left
- `j` move the curosr down one line
- `k` move the cursor up one line
- `l` move the cursor one character right
- `0` move the cursor to the beginning of the line
- `$` move the curosr to the end of the line
- `w` move forward one word 
- `b` move backwards one word
- `G` move to the end of the file
- `gg` move to the beginning of the file
- `\`.` move to the last edit

Prefacing any movement with a number will mean that that movement is done that number of times. For instance, 6w will move forward 6 words.
