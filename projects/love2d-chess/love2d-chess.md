---
title: "Love2D Chess"
description: "A fully-featured chess implementation in Lua using the LÖVE game engine, with complete rule enforcement, special moves, and a polished UI."
date: 2026-03-08
cover: "03-game-moves"
gallery:
  - "01-menu"
  - "02-game-start"
  - "03-game-moves"
  - "04-pawn-promotion"
status: "complete"
featured: true
repo: "https://github.com/Broomfields/Love2D-Chess"
languages: ["Lua"]
dependencies: ["LÖVE 11+", "busted"]
platform: ["Windows", "macOS", "Linux"]
license: "MIT"
tags: ["game", "chess", "love2d"]
credits:
  - label: "Chess piece icons"
    author: "Cburnett"
    url: "https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces"
    license: "CC BY-SA 3.0"
  - label: "Sound effects"
    author: "Kenney"
    url: "https://kenney.nl"
    license: "CC0"
  - label: "OpenDyslexic font"
    author: "Abbie Gonzalez"
    url: "https://opendyslexic.org"
    license: "OFL"
---

Started as a way to properly learn Lua and the LÖVE engine, this project grew into a complete, fully-playable chess implementation. Every rule is enforced — including the ones most amateur implementations skip.

## Features

**Rules & logic**
- Full piece movement with pin detection to prevent illegal moves
- Check detection with visual indicators (red king border, CHECK badge) and audio alert
- Automatic checkmate and stalemate detection
- En passant and castling (kingside and queenside)
- Pawn promotion with deferred turn switching until a piece is selected
- Game resignation with confirmation dialog

**Interface**
- Move notation display above the board
- Dual timers — total game elapsed and per-turn
- Draggable overlay popups for all dialogs
- Sound effects for moves, captures, checks, and UI interactions
- Responsive window scaling for both board and UI elements
- OpenDyslexic font throughout for accessibility

## Running the game

Requires [LÖVE 11+](https://love2d.org).

```bash
love .
```

Unit tests (optional, requires [busted](https://lunarmodules.github.io/busted/)):

```bash
busted spec/
```

## Planned

- Options screen with persistence
- Board scenario loading from data files
- Move history tracking
- Theme customisation
