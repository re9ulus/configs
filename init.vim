call plug#begin('~/.local/share/nvim/plugged')
" NerdTree
Plug 'scrooloose/nerdtree'

" JediVim
Plug 'davidhalter/jedi-vim'

" ctrlp
Plug 'kien/ctrlp.vim'

" lightline
Plug 'itchyny/lightline.vim'

" colorscheme
Plug 'mhartington/oceanic-next'

" Supertab
Plug 'ervandew/supertab'

" CtrlSF
Plug 'dyng/ctrlsf.vim'

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

" FuzzyFileSearch
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'

" Golang
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }

" Ack
Plug 'mileszs/ack.vim'

" Easymotion
Plug 'easymotion/vim-easymotion'

" Goyo, distruction free writing
Plug 'junegunn/goyo.vim'

" Commentary
Plug 'tpope/vim-commentary'

" TypeScript
" # REQUIRED: Add a syntax file. YATS is the best
Plug 'HerringtonDarkholme/yats.vim'
Plug 'mhartington/nvim-typescript', {'do': './install.sh'}
" For async completion
" For Denite features
Plug 'Shougo/denite.nvim'
" EndTypescript

call plug#end()

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
set cursorline
set showmatch

" folding
set foldenable
set foldlevelstart=10
set foldnestmax=10
" space open/close folds
set foldmethod=indent

""" jedi vim config
" let g:jedi#popup_on_dot = 0
" let g:jedi#popup_select_first = 0
let g:jedi#use_splits_not_buffers = "bottom"
" let g:jedi#show_call_signatures = 2

" deoplete is responsible for completion
let g:jedi#completions_enabled = 0
let g:deoplete#sources#jedi#show_docstring = 0

""" START MAPPING

" set leader key
let mapleader="\<Space>"

""" Panes switch hotkeys
map <C-j> <C-W>j
map <C-k> <C-W>k
map <C-h> <C-W>h
map <C-l> <C-W>l

" panel switch
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>

" nerdtee
nmap <leader>ne :NERDTreeToggle<CR>

"folding/unfolding
nnoremap <space>f za

""" END MAPPING

""" Relative line numbers
set relativenumber

""" Golang
let g:go_fmt_command = "goimports"
let g:go_auto_type_info = 1
let g:go_def_mode = 'gopls'
let g:go_info_mode = 'gopls'

""" ColorScheme
" For Neovim 0.1.3 and 0.1.4
let $NVIM_TUI_ENABLE_TRUE_COLOR=1

" Or if you have Neovim >= 0.1.5
if (has("termguicolors"))
 set termguicolors
endif

" Theme
colorscheme OceanicNext
""" EndColorScheme

