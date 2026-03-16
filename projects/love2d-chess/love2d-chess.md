---
title: "Love2D Chess"
description: "A fully-playable chess implementation built in LÖVE — a nostalgia trip back to my first programming language, sparked by the games using Lua that I'd been playing."
date: 2026-03-08
cover: "03-game-moves"
cover_alt: "Chess board mid-game showing move notation, dual timers, and piece positions"
gallery:
  - name: "01-menu"
    label: "Main menu"
  - name: "02-game-start"
    label: "Game start — board at initial position"
  - name: "03-game-moves"
    label: "Mid-game — move notation display and piece move options"
  - name: "04-pawn-promotion"
    label: "Pawn promotion dialog"
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

Lua was my first programming language. I got into it through ComputerCraft, a Minecraft mod, well over a decade ago. At the time I didn't really know what I was doing. I was mimicking what I saw until something worked, which isn't quite the same as understanding it. Same story when I moved on to Minecraft modding in Java.

Years later I came back to Lua properly. And a couple of years ago I decided to finally try LÖVE. Part nostalgia. Part the fact that some games I genuinely respected — Hades, Hades 2, Balatro — were either built in Lua or had it at their core. That felt like a good enough reason.

Chess seemed like a sensible starting point. I worked on it for a couple of weekends, shelved it, and picked it back up two years later to actually finish it. Which, it turns out, means implementing a *lot* of rules.

Every rule is in here. And I mean *every* rule. Chess has more edge cases than you'd expect. Pin detection so you can't make illegal moves even if you try. Check indicators. Automatic checkmate and stalemate. En passant. Both castling directions. Pawn promotion that doesn't accidentally hand off your turn before you've picked a piece.

It also became more of a UI project than expected. Move notation, dual timers, draggable dialogs, sound on every interaction. OpenDyslexic font throughout too, because building that in from the start just makes sense.

## What's in it

**Rules & logic**
- Full piece movement with pin detection to prevent illegal moves
- Check detection with visual indicators (red king border, CHECK badge) and audio alert
- Automatic checkmate and stalemate detection
- En passant and castling (kingside and queenside)
- Pawn promotion with deferred turn switching until a piece is selected
- Game resignation with confirmation dialog

**Interface**
- Move notation display above the board
- Dual timers: total game elapsed and per-turn
- Draggable overlay popups for all dialogs
- Sound effects for moves, captures, checks, and UI interactions
- Responsive window scaling for both board and UI elements
- OpenDyslexic font throughout for accessibility

## Running it

Requires [LÖVE 11+](https://love2d.org).

```bash
love .
```

Unit tests (optional, requires [busted](https://lunarmodules.github.io/busted/)):

```bash
busted spec/
```

## Still on the list

- Options screen with persistence
- Board scenario loading from data files
- Move history tracking
- Theme customisation
