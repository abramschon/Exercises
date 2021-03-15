# Learning Vim

Taken from this [tutorial](https://www.linux.com/training-tutorials/vim-101-beginners-guide-vim/)
See also:
- `vimtutor` (type this into the command line I think)
- (This course)[https://thoughtbot.com/upcase/vim] 

## Modes

Vim has different modes (unofficial names):
- insert mode 
- command mode
- last-line mode

Initially, you are in command mode. To get into insert mode where you can type normally, click `i`. To go out of insert mode, and back into command mode, hit `esc`.

To get into last-line mode, type `:`. From here, you can:
- `w` write the file
- `q` exit the editor

## Navigation

- `h` move the cursor one character left
- `j` move the cursor down one line
- `k` move the cursor up one line
- `l` move the cursor one character right
- `0` move the cursor to the beginning of the line
- `$` move the curosr to the end of the line
- `w` move forward one word 
- `b` move backwards one word
- `gg` move to the beginning of the file
- `G` move to the end of the file
- ``.` move to the last edit

Prefacing any movement with a number will mean that that movement is done that number of times. For instance, 6w will move forward 6 words.

## Editing (while in command mode)

- `x` deletes where cursor is
- `u` undo
- `ctrl+r` redo
- `d` starts delete operation 
- `dd` deletes entire line
- `dw` deletes word
- `d0` deletes until beginning of line
- `d$` deletes until end of line
- `dgg` deletes until beginning of file
- `dG` deletes until end of file 

## Searching and replacing (while in command mode)

- `/text` search for `text` in document going forward
- `n` move cursor to next instance of `text` 
- `N` move cursor to previous instance
- `?text` search for `text` going backward
- `:%s/text/replacement text/g` search through entire document for `text` and replace it with `replacement text` 
- `:%s/text/replacement text/gc` search through document and confirm before replacement

## Copying and pasting

-  
