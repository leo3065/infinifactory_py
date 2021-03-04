"""Classes for manipulating Infinifactory save files.
"""
import base64
import io

from typing import List, Tuple
from .world_blocks import WorldBlocks

from PIL import Image


class Puzzle(object):
    """Class for puzzle in Infinifactory.

    Puzzle keys:
        Title: Title of the puzzle.
        IsAdvanced: True if the puzzle is advanced, False otherwise. 
        Solved: True if the puzzle is solved, False otherwise. 
        PreviewImage: Base64-encoded preview image (512*512) of the puzzle.
            May be absent for puzzles that don't have preview image.
        WorldBlocks: Base64-encoded world block data.
    """

    def __init__(self, title="Untitled Python Puzzle", world_blocks=WorldBlocks({}), preview_image: Image=None, is_advanced=True, solved=False):
        """Constructor.

        Args:
            title: Title of the puzzle
            world_blocks: WorldBlock object describing the blocks in the puzzle
            preview_image: PIL Image 
            is_advanced: Whether the puzzle is made for the advanced puzzle editor, defaults to True, likely should stay that way
            solved: Whether the puzzle was solved, defaults to False, likely should stay that way
        """
        self.title: str = title
        self.world_blocks: WorldBlocks = world_blocks
        self.preview_image: Image = preview_image
        self.is_advanced: bool = is_advanced
        self.solved: bool = solved

    def from_bytes(save_data: bytes):
        """Loads a puzzle from byte data.

        Args:
            save_data: bytes of the puzzle file.
        """
        save_lines = save_data.splitlines()
        save_dict = dict(l.split(b' = ') for l in save_lines)

        title: str = save_dict[b'Title'].decode('utf-8')
        is_advanced = save_dict[b'IsAdvanced'] == b'True'
        solved = save_dict[b'Solved'] == b'True'

        if b'PreviewImage' in save_dict:
            preview_image = Image.open(io.BytesIO(base64.b64decode(save_dict[b'PreviewImage'])))
        else:
            preview_image = None

        world_blocks = WorldBlocks.from_bytes(base64.b64decode(save_dict[b'WorldBlocks']))

        return Puzzle(title, world_blocks, is_advanced, solved, preview_image)

    def from_file(fp: str):
        """Loads a puzzle from a file.

        Args:
            fp: path to a puzzle file.
        """
        with open(fp, "rb") as file:
            return Puzzle.from_bytes(file.read())
