import typer
from pathlib import Path
from silentlovefilter.core.denoiser import clean_audio

app = typer.Typer(add_completion=False)

@app.command()
def main(
    input_path: str = typer.Argument(..., help="Input audio file"),
    output_path: str = typer.Argument(..., help="Output audio file"),
    love_level: int = typer.Option(3, "--love-level", min=1, max=5, help="Denoise intensity (1 mild - 5 aggressive)")
):
    """
    Clean the audio by reducing noise with a love-powered algorithm.

    Args:
        input_file (Path): Path to the input audio file.
        output_file (Path): Path to save the processed audio file.
        love_level (int): Intensity of denoise (1 to 5).

    Returns:
        None
    """
    input_file = Path(input_path)
    output_file = Path(output_path)
    clean_audio(input_file, output_file, love_level)

if __name__ == "__main__":
    app()