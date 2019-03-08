""" Vundle
set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" NerdTree
Plugin 'scrooloose/nerdtree'

" JediVim
Plugin 'davidhalter/jedi-vim'

" ctrlp
Plugin 'kien/ctrlp.vim'

" vim-airline
Plugin 'vim-airline/vim-airline'

" base-16
Plugin 'chriskempson/base16-vim'

" Supertab
Plugin 'ervandew/supertab'

call vundle#end()            " required
filetype plugin indent on    " required
"""

""" Colorscheme
" colorscheme base16-default-dark
" if $COLORTERM == 'gnome-terminal'
"      set t_Co=256
"endif

syntax enable
hi Normal ctermbg=none
highlight NonText ctermbg=none

set tabstop=4
set softtabstop=4
set expandtab
set shiftwidth=4
set smartindent

set number
set wildmenu

set lazyredraw

""" jedi vim config
let g:jedi#popup_on_dot = 0
let g:jedi#popup_select_first = 0

""" Syntactic config
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

""" Panes switch hotkeys
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

""" Relative line numbers
set relativenumber
