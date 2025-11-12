from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from pathlib import Path

console = Console()

def log_info(message: str):
    console.print(Panel(message, style="bold green"))

def log_error(message: str):
    console.print(Panel(message, style="bold red"))

def show_stats(input_file: Path, output_file: Path):
    """Display a comparison table of input and output audio file statistics.

    Shows file sizes in kilobytes for both input and output files in a
    formatted Rich table titled 'Audio Stats'.

    Args:
        input_file (Path): Path to the original input audio file.
        output_file (Path): Path to the processed output audio file.
    """
    table = Table(title="Audio Stats")
    table.add_column("Metric", style="cyan")
    table.add_column("Input", style="magenta")
    table.add_column("Output", style="green")

    input_size = input_file.stat().st_size / 1024
    output_size = output_file.stat().st_size / 1024
    table.add_row("File Size (KB)", f"{input_size:.2f}", f"{output_size:.2f}")

    console.print(table)