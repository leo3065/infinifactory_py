import dataclasses

from infinifactory.face import BlockFacing, DecalFace
from infinifactory.id import BlockID, DecalID

from typing import List, Tuple

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
    position: Tuple[int, int, int]
    facing: BlockFacing
    decals: List[Decal]

class WorldBlocks(object):
    """Class for block strucutes.

    """
    def __init__(self, blocks: List[Block]):
        self.blocks = blocks

    @staticmethod
    def from_bytes(world_block_data: bytes):
        world_block_struct = Struct(
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
    
        parsed_blocks = world_block_struct.parse(world_block_data)
        blocks: List[Block] = []
        for b in parsed_blocks.blocks:
            blocks.append(Block(
                block_id=BlockID(b.block_id),
                position=(b.x, b.y, b.z),
                facing=BlockFacing(b.facing),
                decals=[Decal(
                            decal_id=DecalID(d.decal_id),
                            face=DecalFace(d.face))
                        for d in b.decals]
            ))
        return WorldBlocks(blocks)

