# SilentLoveFilter

A professional command-line tool for audio denoising using FFmpeg. Removes background noise with customizable intensity levels, supports file naming dedication, optional fun ASCII art, and audio previews.

## Features

- Denoise audio files with adjustable "love levels" (1-5) for mild to aggressive noise reduction.
- Custom output file naming with `--dedicate`.
- Preview audio snippets using `pygame` for quick verification.
- Interactive prompts for overwriting existing files.

## Installation

Requires Python 3.8+ and FFmpeg installed on your system.

1. Clone the repository:
   
   ```bash
   git clone https://github.com/RozhakDev/SilentLoveFilter.git
   cd SilentLoveFilter
   ```
2. Install dependencies using Poetry (recommended):
   
   ```bash
   poetry install
   ```
   
    Or with pip:
   
   ```
   pip install typer rich pygame
   ```
   
   > Note: FFmpeg must be installed separately (e.g., `sudo apt install ffmpeg` on Linux).

## Usage

Run commands with `poetry run silentlovefilter` or add to your PATH after installation.

### Clean Audio

Denoise an audio file:

```bash
poetry run silentlovefilter clean input.mp3 output.wav --love-level 4 --dedicate "MyProject" --kiss
```

- Prompts for overwrite if output exists.
- Outputs progress, stats table, and optional ASCII art.

### Preview Audio

```bash
poetry run silentlovefilter preview MyProject_output.wav --seconds 10
```

- Requires `pygame`; installs automatically via dependencies.

For help:

```bash
poetry run silentlovefilter --help
poetry run silentlovefilter clean --help
poetry run silentlovefilter preview --help
```

## License

MIT License. See [LICENSE](LICENSE) for details.