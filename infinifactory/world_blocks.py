import dataclasses

from .face import BlockFacing, DecalFace
from .id import BlockID, DecalID
from .index_utils import is_valid_index_range, is_in_index_range

from typing import List, Tuple, Dict

from construct import Struct, PrefixedArray, Default
from construct import Byte, Int16ul, Int16sl, Int32ul, Const

"""
World block format:

header {03 00 00 00}
block_count uint32
blocks(block_count)[
    block_struct{
        block_type uint16
        x int16
        y int16
        z int16
        facing byte
        counter_setting byte
        stamp_count byte
        decals(decal_count)[
            decal_struct{
                face byte
                decal_type uint16
            }
        ]
    }
]
"""

@dataclasses.dataclass
class Decal(object):
    decal_id: int
    face: DecalFace

@dataclasses.dataclass
class Block(object):
    block_id: int
    facing: BlockFacing
    decals: List[Decal] = dataclasses.field(default_factory=list)
    setting: int = 0

class WorldBlocks(object):
    """Class for block structures."""

    _world_block_struct = Struct(
                Const(b'\x03\x00\x00\x00'),
                'blocks' / PrefixedArray(Int32ul, Struct(
                    'block_id' / Int16ul,
                    'x' / Int16sl,
                    'y' / Int16sl,
                    'z' / Int16sl,
                    'facing' / Byte, 
                    'counter_setting' / Default(Byte, 0),
                    'decals' / Default(PrefixedArray(Byte, Struct(
                        'face' / Byte,
                        'decal_id' / Int16ul
                    )), [])
                ))
            )

    def __init__(self, blocks: Dict[Tuple[int,int,int], Block]):
        """Constructor. 

        Arg:
            blocks: List of blocks to be added.
        """
        self.blocks = blocks

    @staticmethod
    def from_bytes(world_block_data: bytes):
        """Construct a WorldBlocks object from the binary representation.

        Args:
            world_block_data: Binary representation in the save file.
        
        Returns:
            Parsed WorldBlocks object.
        """
        
        parsed_blocks = WorldBlocks._world_block_struct.parse(world_block_data)
        blocks: Dict[Tuple[int,int,int], Block] = {}
        for b in parsed_blocks.blocks:
            blocks[(b.x, b.y, b.z)] = Block(
                block_id=b.block_id,
                facing=BlockFacing(b.facing),
                decals=[Decal(
                            decal_id=d.decal_id,
                            face=DecalFace(d.face))
                        for d in b.decals],
                setting=b.counter_setting
            )
        return WorldBlocks(blocks)

    # Magic methods:
    
    def __bytes__(self):
        blocks = []
        for p, b in self.blocks.items():
            blocks.append({
                'block_id': b.block_id,
                'x': p[0], 'y': p[1], 'z': p[2],
                'facing': int(b.facing),
                'decals': [
                    {'face': d.face, 'decal_id': d.decal_id}
                    for d in b.decals
                ],
                'counter_setting': b.setting
            })
        return self._world_block_struct.build({'blocks': blocks})

    def __bool__(self):
        return self.blocks != {}
    
    def __len__(self):
        return len(self.blocks)
    
    def __getitem__(self, key):
        if not is_valid_index_range(key):
            raise TypeError('The key must be a valid index range.')

        if all(isinstance(v, int) for v in key):
            return self.blocks[key]
        
        blocks: Dict[Tuple[int,int,int], Block] = {}
        for pos, block in self.blocks.items():
            if is_in_index_range(pos, key):
                blocks[pos] = block
        return WorldBlocks(blocks)
    
    def __setitem__(self, key, value):
        if not is_valid_index_range(key):
            raise TypeError('The key must be a valid index range.')
        if not isinstance(value, Block):
            raise TypeError('The value must be a block.')
        
        if all(isinstance(v, int) for v in key):
            self.blocks[key] = value
            return
        
        for pos in self.blocks.keys():
            if is_in_index_range(pos, key):
                self.blocks[pos] = value

    def __delitem__(self, key):
        if not is_valid_index_range(key):
            raise TypeError('The key must be a valid index range.')

        if all(isinstance(v, int) for v in key):
            del self.blocks[key]
            return
        
        poses = list(self.blocks.keys())
        for pos in poses:
            if is_in_index_range(pos, key):
                del self.blocks[pos]

    def __contains__(self, key):
        return key in self.blocks

    def __iter__(self):
        return iter(self.blocks)

    def keys(self):
        return self.blocks.keys()

    def items(self):
        return self.blocks.items()

    def values(self):
        return self.blocks.values()
