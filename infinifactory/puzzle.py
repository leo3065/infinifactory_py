"""Classes for manipulating Infinifactory save files.
"""
import base64
import io

from typing import List, Tuple, Dict, Optional, Any
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

    def __init__(
        self,
        title="Untitled Python Puzzle",
        world_blocks=WorldBlocks({}),
        preview_image: Optional[Image.Image]=None,
        is_advanced=True, solved=False,
        # The following argument is keyword only
        *, extra_params: Optional[Dict[str,Any]]):
        """Constructor.

        Args:
            title: Title of the puzzle
            world_blocks: WorldBlock object describing the blocks in the puzzle
            preview_image: PIL Image, or None if missing
            is_advanced: Whether the puzzle is made for the advanced puzzle editor, defaults to True, likely should stay that way
            solved: Whether the puzzle was solved, defaults to False, likely should stay that way

            extra_params: The extra unhandled parameters in the puzzle
        """
        self.title: str = title
        self.world_blocks: WorldBlocks = world_blocks
        self.preview_image: Optional[Image.Image] = preview_image
        self.is_advanced: bool = is_advanced
        self.solved: bool = solved
        self.extra_params: Dict[str,Any] = extra_params if extra_params is not None else {}

    @staticmethod
    def from_str(save_data: str):
        """Loads a puzzle from byte data.

        Args:
            save_data: str of the puzzle file.
        """
        save_lines = save_data.splitlines()
        save_dict = dict(l.split(' = ') for l in save_lines)

        title: str = save_dict['Title']
        is_advanced = save_dict['IsAdvanced'] == 'True'
        solved = save_dict['Solved'] == 'True'

        if 'PreviewImage' in save_dict:
            preview_image = Image.open(io.BytesIO(base64.b64decode(save_dict['PreviewImage'])))
        else:
            preview_image = None

        world_blocks = WorldBlocks.from_bytes(base64.b64decode(save_dict['WorldBlocks']))

        handled_keys = [
            'Title',
            'Solved',
            'IsAdvanced',
            'PreviewImage',
            'WorldBlocks',
            ]
        return Puzzle(title, world_blocks, preview_image, is_advanced, solved,
            extra_params={k: v for k, v in save_dict.items() if k not in handled_keys})

    @staticmethod
    def from_file(fp: str):
        """Loads a puzzle from a file.

        Args:
            fp: path to a puzzle file.
        """
        with open(fp, "r") as file:
            return Puzzle.from_str(file.read())

    def __str__(self):
        """Returns the string representation of this object.
        """
        save_dict = self.extra_params.copy()
        save_dict['Title'] = self.title
        save_dict['IsAdvenced'] = self.is_advanced
        save_dict['Solved'] = self.solved
        save_dict['WorldBlocks'] = base64.b64encode(bytes(self.world_blocks)).decode("utf-8")

        return ''.join(f'{k} = {save_dict[k]}\n' for k in sorted(save_dict.keys()))

    def to_file(self, fp: str, allow_overwrite=False):
        """Writes the puzzle to a file.

        Args:
            fp: path to the puzzle file.
            allow_overwrite: whether to overwrite the file if it exists.
        """
        with open(fp, "w", encoding="utf-8") as file:
            file.write(str(self))
