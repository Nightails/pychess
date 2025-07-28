# PyChess ♟️

Play chess in the terminal!

Written in Python, this project is made in part of [Boot.dev](https://boot.dev) Hackathon July 2025

> [!NOTE]
> This is still a work-in-progress with missing features.

## Requirements

- **Python**: 3.13+
- **Package Manager**: [uv](https://docs.astral.sh/uv/) (recommended for managing dependencies)
- **Platform**: ✔️Linux, ❓macOS, ❓Windows

### Dependencies

- [textual](https://textual.textualize.io/) - python terminal ui library
- [rich](https://rich.readthedocs.io/en/latest/) - python library for rendering rich text
- [pygame](https://www.pygame.org/docs/) - python game framework library

## Install & Setup

1. **Install uv**

```
# Linux and macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. **Clone the repository**

```
git clone https://github.com/Nightails/pychess.git
cd pychess
```

3. **Install dependencies** (optional - uv takes care of it)

```
# Install project dependencies
uv install
```

4. **Run PyChess**

```
uv run main.py
```

## Roadmap & Personal Note

1. **To-do**:
- [ ] Move rule
- [ ] Piece taking
- [ ] AI opponents
- [ ] Multiplayer
- [ ] Theme

2. **Notes**:

This project was hastily put together over a 3 days weekend. So existence of [python-chess](https://python-chess.readthedocs.io/en/latest/) was unknown to me until recently. It is more reason to finish this someday with my own back-end for handling: moves validation, rules, and check-mate checking, etc.

Front-end is being handled by textual. Though more research still need to be done, as I's exposed to the library for only 2 days.

Contributions are welcome!

PyChess is under MIT license.
