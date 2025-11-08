import subprocess
import sys
from typing import Literal
from pathlib import Path
from rich.progress import Progress
from rich.console import Console

console = Console()

def clean_audio(input_file: Path, output_file: Path, love_level: Literal[1, 2, 3, 4, 5] = 3) -> None:
    """Clean the audio by reducing background noise using FFmpeg.

    This function applies a series of filters (high-pass, low-pass, and adaptive denoise)
    based on the specified love_level to reduce unwanted noise from the input audio file.

    Args:
        input_file (Path): The input audio file to process.
        output_file (Path): The path where the cleaned audio will be saved.
        love_level (Literal[1, 2, 3, 4, 5], optional): Denoising intensity (1 = mild, 5 = strong).

    Raises:
        SystemExit: If the input file does not exist or FFmpeg processing fails.
    """
    if not input_file.exists():
        console.print(f"[bold red]Error: Input file '{input_file} not found.[/]'")
        sys.exit(1)

    # Preset noise floor based on love_level
    nf = -10 - (love_level - 1) * 5  # -10 to -30

    cmd = [
        "ffmpeg", "-y", "-i", str(input_file),  
        "-af", f"highpass=f=80,lowpass=f=4000,afftdn=nf={nf}",  
        str(output_file)
    ]

    console.print("[bold green]Starting audio denoising...[/]")
    console.print(f"[cyan]Love level: {love_level} (Noise floor: {nf} dB)[/]")

    with Progress(console=console, transient=True) as progress:  
        task = progress.add_task("[cyan]Processing audio...", total=None)  
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)  
        progress.update(task, completed=True)  
  
    if result.returncode != 0:  
        console.print("[bold red]FFmpeg error:[/]")  
        console.print(result.stderr)  
        sys.exit(1)  
  
    console.print("[bold green]Denoising complete![/]")  
    console.print(f"[green]Output: {output_file} (Size: {output_file.stat().st_size / 1024:.2f} KB)[/]")