from enum import IntEnum

class BlockFacing(IntEnum):
    PosZ = 0
    NegX = 1
    NegZ = 2
    PosX = 3

    def rotate_ccw(self):
        return BlockFacing((self+1)%4)

    def rotate_cw(self):
        return BlockFacing((self-1)%4)

class DecalFace(IntEnum):
    Right = 0
    Left = 1
    Bottom = 2
    Top = 3
    Front = 4
    Back = 5
    
    def rotate_ccw(self):
        ccw_table = {
            DecalFace.Right: DecalFace.Front,
            DecalFace.Left: DecalFace.Back,
            DecalFace.Bottom: DecalFace.Bottom,
            DecalFace.Top: DecalFace.Top,
            DecalFace.Front: DecalFace.Left,
            DecalFace.Back: DecalFace.Right,
        }
        return ccw_table[self]
        
    def rotate_cw(self):
        cw_table = {
            DecalFace.Right: DecalFace.Back,
            DecalFace.Left: DecalFace.Front,
            DecalFace.Bottom: DecalFace.Bottom,
            DecalFace.Top: DecalFace.Top,
            DecalFace.Front: DecalFace.Right,
            DecalFace.Back: DecalFace.Left,
        }
        return cw_table[self]