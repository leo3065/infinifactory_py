"""Classes for manimulating Infinifacoty save files.
"""
import base64
import io

from typing import List, Tuple

from PIL import Image


class Puzzle(object):
    """Class for puzzle in Infinifacoty.

    Puzzle keys:
        Title: Title of the puzzle.
        IsAdvanced: True if the puzzle is advenced, False otherwise. 
        Solved: True if the puzzle is solved, False otherwise. 
        PreviewImage: Base64-encoded preview image (512*512) of the puzzle.
            May be absent for puzzles that doesn't have preview image.
        WorldBlocks: Base64-encoded world block data.
    """

    def __init__(self, save_data: bytes):
        """Constructor.

        Args:
            save_data: bytes of the puzzle file.
        """
        save_lines = save_data.splitlines()
        save_dict = dict(l.split(b' = ') for l in save_lines)

        self.title: str = save_dict[b'Title'].decode('utf-8')
        self.is_advenced = save_dict[b'IsAdvanced'] == b'True'
        self.solved = save_dict[b'Solved'] == b'True'

        if b'PreviewImage' in save_dict:
            self.preview_image = Image.open(io.BytesIO(
                base64.b64decode(save_dict[b'PreviewImage'])))
        else:
            self.preview_image = None
