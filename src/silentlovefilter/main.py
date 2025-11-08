import subprocess
import sys
from pathlib import Path
import typer
from rich.console import Console

app = typer.Typer(add_completion=False)
console = Console()

def clean_audio(input_file: Path, output_file: Path):
    if not input_file.exists():
        console.print(f"[bold red]Error: File not found → {input_file}[/]")
        raise typer.Exit(1)

    cmd = [
        "ffmpeg", "-y", "-i", str(input_file),
        "-af", "highpass=f=80,lowpass=f=4000,afftdn=nf=-25",
        str(output_file)
    ]
    
    console.print("[bold cyan]Cleaning audio...[/]")
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode != 0:
        console.print("[bold red]FFmpeg error:[/]")
        console.print(result.stderr)
        raise typer.Exit(1)
    
    console.print("[bold green]Done! →[/] " + str(output_file))

@app.command()
def main(
    input: Path = typer.Argument(..., help="Input audio file"),
    output: Path = typer.Argument(..., help="Output audio file")
):
    clean_audio(input, output)

if __name__ == "__main__":
    app()