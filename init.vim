call plug#begin('~/.local/share/nvim/plugged')
" NerdTree
Plug 'scrooloose/nerdtree'

" JediVim
Plug 'davidhalter/jedi-vim'

" ctrlp
Plug 'kien/ctrlp.vim'

" vim-airline
Plug 'vim-airline/vim-airline'

" base-16
Plug 'chriskempson/base16-vim'

" Supertab
Plug 'ervandew/supertab'

" YouCompleteMe
" If it fails with `The ycmd server SHUT DOWN` then run /usr/bin/python install.py in ~/.vim/plugged/YouCompleteMe
" Plug 'Valloric/YouCompleteMe'

" Deoplete
if has('nvim')
  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
else
  Plug 'Shougo/deoplete.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
Plug 'deoplete-plugins/deoplete-jedi'  " python

" clang configuration
let g:deoplete#sources#clang#libclang_path = '/usr/lib/llvm-8/lib/libclang-8.so.1'
let g:deoplete#sources#clang#clang_header = '/usr/lib/llvm-8/include'
Plug 'zchee/deoplete-clang'

let g:deoplete#enable_at_startup = 1
" End deoplete

" Clang
" Plug 'xavierd/clang_complete'

" FuzzyFileSearch
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'

call plug#end()

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

" set lazyredraw

""" jedi vim config
let g:jedi#popup_on_dot = 0
let g:jedi#popup_select_first = 0

""" Syntactic config
" set statusline+=%#warningmsg#
" set statusline+=%{SyntasticStatuslineFlag()}
" set statusline+=%*
" let g:syntastic_always_populate_loc_list = 1
" let g:syntastic_auto_loc_list = 1
" let g:syntastic_check_on_open = 1
" let g:syntastic_check_on_wq = 0

""" Panes switch hotkeys
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

""" Relative line numbers
set relativenumber
