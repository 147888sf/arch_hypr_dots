vim.g.mapleader = ' '

vim.opt.number = true -- Line numbers
vim.opt.mouse = 'a' -- Mouse support
vim.opt.clipboard = 'unnamedplus' -- System clipboard
vim.opt.ignorecase = true -- Ignore case in search
vim.opt.smartcase = true -- Smart case in search
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4 -- Tab size
vim.opt.expandtab = true -- Insert spaces instead of tab
vim.opt.termguicolors = true -- 24-bit colors support

-- Plugins
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
  -- Status bar
  {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons' },
    defaults = {
      vimgrep_arguments = {
        "rg",
        "--hidden",
        "--no-ignore",
        "--color=never",
        "--no-heading",
        "--with-filename",
        "--line-number",
        "--column",
        "--smart-case",
      },

      file_ignore_patterns = {
        ".git/",
      },
    },

    config = function()
      require('lualine').setup({
        options = { theme = 'auto' },
        sections = {
          lualine_a = { "mode" },
          lualine_b = { "branch", "diff", "diagnostics" },
          lualine_c = { {"filename", path = 1} },
          lualine_x = {  },
          lualine_y = {  },
          lualine_z = {  },
        },
      })
    end
  },

  -- Search 
  {
    'nvim-telescope/telescope.nvim',
    dependencies = { 'nvim-lua/plenary.nvim' },
    config = function()
      local telescope = require('telescope')
      telescope.setup()
      local builtin = require('telescope.builtin')
      vim.keymap.set('n', '<leader>ff', builtin.find_files, {})
      vim.keymap.set('n', '<leader>fg', builtin.live_grep, {})
      vim.keymap.set('n', '<leader>fb', builtin.buffers, {})
      vim.keymap.set('n', '<leader>fh', builtin.help_tags, {})
    end
  },
  
  -- Tabs
  {
    'akinsho/bufferline.nvim',
    version = "*",
    dependencies = 'nvim-tree/nvim-web-devicons',
    config = function()
      require("bufferline").setup{
        options = {
          mode = "buffers",
          separator_style = "thick",
          show_close_icon = false,
        }
      }

      vim.keymap.set('n', '<Tab>', '<Cmd>BufferLineCycleNext<CR>', {})
    end
  },
  
  -- File tree  
  {
    'nvim-tree/nvim-tree.lua',
    dependencies = { 'nvim-tree/nvim-web-devicons' },
    config = function()
      require('nvim-tree').setup()
      vim.keymap.set('n', '<leader>t', ':NvimTreeToggle<CR>', { silent = true })
    end
  },

  -- Auto complete
  {
    'hrsh7th/nvim-cmp',
    dependencies = {
      'hrsh7th/cmp-nvim-lsp',
      'hrsh7th/cmp-buffer',
      'hrsh7th/cmp-path',
      'hrsh7th/cmp-cmdline',
      'saadparwaiz1/cmp_luasnip',
    },

    config = function()
      local cmp = require('cmp')
      cmp.setup({
        snippet = {
          expand = function(args)
            require('luasnip').lsp_expand(args.body)
          end,
        },
        mapping = cmp.mapping.preset.insert({
          ['<C-j>'] = cmp.mapping.select_next_item(),
          ['<C-k>'] = cmp.mapping.select_prev_item(),
          ['<C-e>'] = cmp.mapping.abort(),
          ['<CR>'] = cmp.mapping.confirm({ select = true }),
        }),
        sources = cmp.config.sources({
          { name = 'luasnip', priority = 1000 },
          { name = 'nvim_lsp', priority = 900 },
          { name = 'buffer', priority = 500 },
          { name = 'path' },
        }),
      })
    end
  },

  -- Snippets
  {
    'L3MON4D3/LuaSnip',
    dependencies = {
      'rafamadriz/friendly-snippets',
    },
    config = function()
      require('luasnip.loaders.from_vscode').lazy_load()
    end
  },

  -- LSP
  {
    'williamboman/mason.nvim',
    config = function()
      require('mason').setup()
    end
  },
  {
    'williamboman/mason-lspconfig.nvim',
    config = function()
      require('mason-lspconfig').setup({
        ensure_installed = { 'lua_ls', 'pyright', 'rust_analyzer' }
      })
    end
  },
  {
    'neovim/nvim-lspconfig',
    config = function()
      local lspconfig = require('lspconfig')
      lspconfig.lua_ls.setup({})
      lspconfig.pyright.setup({})
      lspconfig.rust_analyzer.setup({})
      vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, {})
      vim.keymap.set('n', 'gd', vim.lsp.buf.definition, {})
      vim.keymap.set('n', 'K', vim.lsp.buf.hover, {})
      vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, {})
      vim.keymap.set('n', '<leader>rn', vim.lsp.buf.rename, {})
      vim.keymap.set('n', '<leader>ca', vim.lsp.buf.code_action, {})
    end
  },

  -- Comments
  {
    'tpope/vim-commentary',
  },

  -- Color scheme
  { "navarasu/onedark.nvim" }
})

vim.keymap.set('n', '<leader>`', '<cmd>botright terminal<cr>')
vim.keymap.set('n', '<leader>q', '<cmd>botright terminal python3 %<cr>')
vim.keymap.set('n', '<leader>w', '<cmd>bd<cr>')
vim.keymap.set('n', '<leader>fw', '<cmd>bd!<cr>')
vim.keymap.set('n', '<leader>e', ':wincmd w<CR>', { noremap = true, silent = true })
vim.keymap.set('v', '<Tab>', '>gv', { noremap = true })
vim.keymap.set('v', '<S-Tab>', '<gv', { noremap = true })
vim.keymap.set({ 'n', 'v' }, '<C-/>', ':Commentary<CR>', { noremap = true })

vim.cmd.colorscheme("onedark")
