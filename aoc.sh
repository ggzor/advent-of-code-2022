#!/usr/bin/env bash

set -euo pipefail

validate() {
  if [[ -e "${COOKIE}" ]]; then
    exit_error "No \$COOKIE was set"
  fi

  if (( $# < 1 || $# > 2 )) || [[ ! $1 =~ ^(setup|watch|post)$ ]]; then
    exit_error "Wrong command. Expected setup|watch|post <level>, got '${1:-}'"
  fi

  COMMAND=$1
  if (( $# == 2 )); then
    ARG=$2
  fi
  DAY=$(printf '%02d' "${DAY:-$(date +'%d')}")
  YEAR=$(printf '%02d' "${YEAR:-$(date +'%Y')}")

  if [[ ! $DAY =~ [0-9]+ ]] || (( 10#$DAY < 1 || 10#$DAY > 25 )); then
    exit_error "\$DAY must be a number between 1 and 25: Got '$DAY'"
  fi
}

main() {
  local TARGET_INPUT="$DAY/input.txt"
  local DEFAULT_SOLVER="python -m '$DAY.$DAY'"

  export AOC_INPUT=${AOC_INPUT:-"$TARGET_INPUT"}

  case $COMMAND in
    setup)
      mkdir -p "$DAY"

      # Python
      touch "$DAY/__init__.py"
      cp_if_needed 'templates/template.py' "$DAY/$DAY.py"

      # Download input
      if [[ ! -f "$TARGET_INPUT" ]]; then
        info "Downloading input..."
        curl -sfL --cookie "$COOKIE" \
          "https://adventofcode.com/$YEAR/day/$((10#$DAY))/input" \
          > "$TARGET_INPUT"
      else
        info "Input already downloaded"
      fi

      success "$DAY of $YEAR setup"
      ;;
    watch)
      printf '%s\n' "$AOC_INPUT" "$DAY/$DAY.py" \
        | entr -rc bash -c "tput clear; $DEFAULT_SOLVER"
      ;;
    post)
      local LEVEL=${ARG:-1}
      local OUTPUT
      OUTPUT=$(bash -c "$DEFAULT_SOLVER" | tail -1)

      printf '\e[1;34mInfo:\e[0m Posting answer - "\e[1m%s\e[0m"\n' "$OUTPUT"
      curl -fL -X POST --cookie "$COOKIE" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        --data-urlencode "level=$LEVEL" \
        --data-urlencode "answer=$OUTPUT" \
        "https://adventofcode.com/$YEAR/day/$((10#$DAY))/answer"
      ;;
    *)
      exit_error "Unknown command '$COMMAND'"
      ;;
  esac
}

cp_if_needed() {
  local SRC=$1
  local DEST=$2

  if [[ -f "$DEST" ]]; then
    info "File '$DEST' already exists, skipping"
  else
    cp "$SRC" "$DEST"
  fi
}

info() {
  printf '\e[2mInfo: %s\e[0m\n' "$1"
}

success() {
  printf '\e[1;32mSuccess:\e[0m %s\n' "$1"
}

exit_error() {
  printf '\e[1;31mError:\e[0m %s\n' "$1"
  exit 1
}

validate "$@"
main
