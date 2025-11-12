import subprocess
import sys
from typing import Literal
from pathlib import Path
from rich.progress import Progress
from silentlovefilter.utils.logger import console, log_info, log_error, show_stats

def clean_audio(input_file: Path, output_file: Path, love_level: Literal[1, 2, 3, 4, 5] = 3) -> None:
    """Denoise an audio file using FFmpeg with adaptive noise-floor reduction.

    Applies a high-pass filter (80 Hz), low-pass filter (4 kHz), and
    frequency-domain noise suppression using FFmpeg's `afftdn` filter.
    The noise floor level is determined by the `love_level` parameter.

    Args:
        input_file (Path): Path to the source audio file. Must exist.
        output_file (Path): Path to save the denoised audio file.
        love_level (Literal[1, 2, 3, 4, 5], optional): Aggressiveness of
            noise reduction. Level 1 is mild (-10 dB), level 5 is strong (-30 dB).
            Defaults to 3.

    Raises:
        SystemExit: If the input file does not exist or FFmpeg fails.
    """
    if not input_file.exists():
        log_error(f"Input file '{input_file}' not found.")
        sys.exit(1)

    nf = -10 - (love_level - 1) * 5

    cmd = ["ffmpeg", "-y", "-i", str(input_file), "-af", f"highpass=f=80,lowpass=f=4000,afftdn=nf={nf}", str(output_file)]

    log_info("Starting audio denoising...")
    console.print(f"[cyan]Love level: {love_level} (Noise floor: {nf} dB)[/]")

    with Progress(console=console, transient=True) as progress:
        task = progress.add_task("[cyan]Processing audio...", total=None)
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        progress.update(task, completed=True)

    if result.returncode != 0:
        log_error("FFmpeg processing failed:")
        console.print(result.stderr)
        sys.exit(1)

    log_info("Denoising complete!")
    show_stats(input_file, output_file)