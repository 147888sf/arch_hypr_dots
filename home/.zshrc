source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
ZSH_AUTOSUGGEST_STRATEGY=(completion)

bindkey "^[[3~" delete-char
bindkey "^[[1;5D" backward-word
bindkey "^[[1;5C" forward-word
bindkey '^H' backward-kill-word
bindkey '^[[3;5~' kill-word

HISTFILE=~/.zsh_history
HISTSIZE=1000
SAVEHIST=1000
setopt hist_ignore_all_dups
setopt INC_APPEND_HISTORY
setopt SHARE_HISTORY

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias reload='clear && source ~/.zshrc'
alias lsa='ls -A'
alias fetch='fastfetch'

alias g="git"
alias b="bat"
alias rm="trash-put"
alias rmF="rm"
alias pac="sudo pacman"
alias stat="cloc ."

autoload -U compinit
compinit

fastfetch
eval "$(oh-my-posh init zsh --config ~/.config/oh-my-posh/themes/custom_config.omp.json)"