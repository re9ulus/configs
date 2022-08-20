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

" CtrlSF
Plug 'dyng/ctrlsf.vim'

" Nim
Plug 'alaviss/nim.nvim'

" Autocomplete (instead deoplete)
Plug 'neoclide/coc.nvim', {'branch': 'release'}
" rust
Plug 'rust-lang/rust.vim'

" FuzzyFileSearch
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'

" Golang
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }

" Ack
Plug 'mileszs/ack.vim'

" Commentary
Plug 'tpope/vim-commentary'

" Telescope
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

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

""" Relative line numbers
set relativenumber

""" jedi vim config
let g:jedi#use_splits_not_buffers = "bottom"
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

" FZF
nnoremap <leader>f :FZF<CR>

" nerdtee
nmap <leader>ne :NERDTreeToggle<CR>

" quicksave
nmap <leader>w :w<CR>

" quick tab toggle
nmap <leader><leader> <c-^>

"folding/unfolding
" nnoremap <space>f za

""" END MAPPING


""" CocConfig
" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>


function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  elseif (coc#rpc#ready())
    call CocActionAsync('doHover')
  else
    execute '!' . &keywordprg . " " . expand('<cword>')
  endif
endfunction

" Coc autocomplete config
" https://github.com/neoclide/coc.nvim/pull/3862
inoremap <silent><expr> <CR> coc#pum#visible() ? coc#pum#confirm() : "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"
inoremap <silent><expr> <C-x><C-z> coc#pum#visible() ? coc#pum#stop() : "\<C-x>\<C-z>"
" remap for complete to use tab and <cr>
inoremap <silent><expr> <TAB>
  \ coc#pum#visible() ? coc#pum#next(1):
  \ <SID>check_back_space() ? "\<Tab>" :
  \ coc#refresh()
inoremap <expr><S-TAB> coc#pum#visible() ? coc#pum#prev(1) : "\<C-h>"
inoremap <silent><expr> <c-space> coc#refresh()

hi CocSearch ctermfg=12 guifg=#18A3FF
hi CocMenuSel ctermbg=109 guibg=#13354A

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" Don't pass messages to |ins-completion-menu|.
set shortmess+=c

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)
""" EndCocConfig


""" Golang
let g:go_fmt_command = "goimports"
let g:go_auto_type_info = 1
let g:go_def_mode = 'gopls'
let g:go_info_mode = 'gopls'
" required to correct work of go-coc and vim-go
let g:go_def_mapping_enabled = 0

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

""" Configure telescope
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>
