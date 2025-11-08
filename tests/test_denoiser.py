from silentlovefilter.core.denoiser import clean_audio
from pathlib import Path
import pytest

def test_clean_audio(tmp_path):
    # Assume sample input exists; in real, provide a small audio file
    input_file = tmp_path / "input.mp3"
    input_file.write_bytes(b"fake audio data") # Dummy for test
    output_file = tmp_path / "output.wav"

    with pytest.raises(SystemExit): # Expect FFmpeg fail on dummy, but test flow
        clean_audio(input_file, output_file, love_level=3)