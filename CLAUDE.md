# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal Pokemon tracking repository for Pokemon GO. It contains:
- A master Pokedex list of Pokemon IDs (`pokedex.md`)
- League-specific tracking organized by Pokemon generation (`leagues/gen-N-region/`)
- PvE content tracking (`pve/`)

## Repository Structure

```
pokemon/
├── pokedex.md              # Master list of Pokemon IDs (comma-separated)
├── leagues/                # Generation-specific league tracking
│   ├── gen-1-kanto/
│   ├── gen-2-johto/
│   ├── gen-3-hoenn/
│   ├── gen-4-sinnoh/
│   ├── gen-5-unova/
│   ├── gen-6-kalos/
│   ├── gen-7-alola/
│   ├── gen-8-galar-and-hisui/
│   └── gen-9-paldea/
└── pve/                    # PvE content (currently empty)
```

## Data Format

### pokedex.md
- Contains a comma-separated list of Pokemon IDs (National Dex numbers)
- Format: `1, 6, 7, 23, 25, ...`
- No headers or metadata, just the raw ID list

## Working with This Repository

### Adding Pokemon IDs
- Maintain numeric order when adding new IDs to `pokedex.md`
- Use comma-separated format with spaces after commas
- Keep all IDs on a single line

### League Organization
- Each generation has its own subdirectory under `leagues/`
- Directory naming: `gen-{number}-{region}` (e.g., `gen-1-kanto`)
- Generation 8 combines Galar and Hisui regions

## Context

This is a personal tracking repository with minimal structure. There are no build commands, tests, or code to execute. All operations are simple file reads and writes to track Pokemon data.
