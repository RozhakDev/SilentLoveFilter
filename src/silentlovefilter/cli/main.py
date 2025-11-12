import typer
from pathlib import Path
from typing import Optional
from silentlovefilter.core.denoiser import clean_audio
from silentlovefilter.utils.ascii_kiss import get_kiss
from silentlovefilter.utils.logger import console

app = typer.Typer(help="SilentLoveFilter: Professional Audio Denoising CLI")

@app.command()
def clean(
    input: Path = typer.Argument(..., help="Input audio file"),
    output: Path = typer.Argument(..., help="Output audio file"),
    love_level: int = typer.Option(3, "--love-level", min=1, max=5, help="Denoising intensity (1 mild - 5 aggressive)"),
    dedicate: Optional[str] = typer.Option(None, "--dedicate", help="Custom prefix for output file name"),
    kiss: bool = typer.Option(False, "--kiss", help="Display fun ASCII art on completion (optional)"),
):
    """Denoise an audio file with customizable intensity and optional flair.

    Applies professional-grade spectral noise reduction using FFmpeg.
    Supports output file confirmation, custom naming via dedication,
    and a playful kiss emoticon on completion.

    Args:
        input (Path): Path to the source audio file.
        output (Path): Desired path for the denoised output file.
        love_level (int): Denoising aggressiveness from 1 (mild) to 5 (aggressive).
        dedicate (Optional[str]): If provided, prepends this string to the output file name.
        kiss (bool): If True, displays a random affectionate ASCII-style kiss after processing.
    """
    if output.exists() and not typer.confirm(f"Overwrite existing file '{output}'?", default=True):
        console.print("[yellow]Operation cancelled.[/]")
        raise typer.Exit()

    if dedicate:
        output = output.with_stem(f"{dedicate}_{output.stem}")

    clean_audio(input, output, love_level)

    if kiss:
        console.print(f"[magenta]{get_kiss()}[/]")

@app.command()
def preview(
    file: Path = typer.Argument(..., help="Audio file to preview"),
    seconds: int = typer.Option(5, "--seconds", min=1, help="Duration of preview in seconds"),
):
    """Play a short audible preview of an audio file using pygame.

    Intended for quick verification before or after denoising.
    Requires `pygame` to be installed. Falls back with a helpful error
    message if dependencies are missing.

    Args:
        file (Path): Path to the audio file to preview.
        seconds (int): Number of seconds to play (minimum 1).

    Raises:
        typer.Exit: If the file does not exist or pygame is not available.
    """
    if not file.exists():
        console.print("[bold red]Error: File not found.[/]")
        raise typer.Exit(1)

    try:
        import pygame
        import time
        
        console.print(f"[cyan]Playing {seconds} seconds preview of '{file}'...[/]")
        
        pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
        pygame.mixer.init()
        
        pygame.mixer.music.load(str(file))
        pygame.mixer.music.play()
        
        time.sleep(seconds)
        
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        
        console.print(f"[green]Successfully played {seconds} seconds preview![/]")
        
    except ImportError:
        console.print("[bold red]Error: Required packages not installed. Run 'pip install pygame' to enable audio preview.[/]")
        raise typer.Exit(1)
    except Exception as e:
        console.print(f"[bold red]Error playing audio: {str(e)}[/]")
        console.print(f"[yellow]Preview would play for {seconds} seconds but encountered an error. The clean command works fine![/]")

if __name__ == "__main__":
    app()