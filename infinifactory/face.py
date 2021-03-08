from enum import IntEnum

class BlockFacing(IntEnum):
    """Enums for rotation of block, using the "front" face.
    """
    PosZ = 0
    NegX = 1
    NegZ = 2
    PosX = 3

    def __str__(self):
        name_dict = {
            BlockFacing.PosZ: 'PosZ',
            BlockFacing.NegX: 'NegX',
            BlockFacing.NegZ: 'NegZ',
            BlockFacing.PosX: 'PosX',
        }
        return name_dict[self]
    
    def rotate_ccw(self, angle: int = 1):
        """Rotating the facing counterclockwise. 
        
        Arg:
            Angle of rotation, where 1 is 90 deg.
        """
        return BlockFacing((self+angle)%4)

    def rotate_cw(self, angle: int = 1):
        """Rotating the facing clockwise. 
        
        Arg:
            Angle of rotation, where 1 is 90 deg.
        """
        return BlockFacing((self-angle)%4)

class DecalFace(IntEnum):
    """Enums for face for decal, which is in relative (block based) coordinate.
    """
    Right = 0
    Left = 1
    Bottom = 2
    Top = 3
    Front = 4
    Back = 5

    def __str__(self):
        name_dict = {
            DecalFace.Right: 'Right',
            DecalFace.Left: 'Left',
            DecalFace.Bottom: 'Bottom',
            DecalFace.Top: 'Top',
            DecalFace.Front: 'Front',
            DecalFace.Back: 'Back',
        }
        return name_dict[self]
    
    def rotate_ccw(self, angle: int = 1):
        """Rotating the face counterclockwise. 
        
        Arg:
            Angle of rotation, where 1 is 90 deg.
        """
        ccw_table = {
            DecalFace.Right: DecalFace.Front,
            DecalFace.Left: DecalFace.Back,
            DecalFace.Bottom: DecalFace.Bottom,
            DecalFace.Top: DecalFace.Top,
            DecalFace.Front: DecalFace.Left,
            DecalFace.Back: DecalFace.Right,
        }
        face = self
        for i in range(angle%4):
            face = ccw_table[face]
        return face
        
    def rotate_cw(self, angle: int = 1):
        """Rotating the face clockwise. 
        
        Arg:
            Angle of rotation, where 1 is 90 deg.
        """
        cw_table = {
            DecalFace.Right: DecalFace.Back,
            DecalFace.Left: DecalFace.Front,
            DecalFace.Bottom: DecalFace.Bottom,
            DecalFace.Top: DecalFace.Top,
            DecalFace.Front: DecalFace.Right,
            DecalFace.Back: DecalFace.Left,
        }
        face = self
        for i in range(angle%4):
            face = cw_table[face]
        return face
    
    def to_absolute(self, dir: BlockFacing):
        return AbsoluteFacing(int(self.rotate_cw(int(dir))))


class AbsoluteFacing(IntEnum):
    """Enums for absolute (world coordinate) direction.
    """
    PosX = 0
    NegX = 1
    NegY = 2
    PosY = 3
    PosZ = 4
    NegZ = 5

    def __str__(self):
        name_dict = {
            AbsoluteFacing.PosX: 'PosX',
            AbsoluteFacing.NegX: 'NegX',
            AbsoluteFacing.NegY: 'NegY',
            AbsoluteFacing.PosY: 'PosY',
            AbsoluteFacing.PosZ: 'PosZ',
            AbsoluteFacing.NegZ: 'NegZ',
        }
        return name_dict[self]
        
    def rotate_ccw(self, angle: int = 1):
        """Rotating the direction counterclockwise. 
        
        Arg:
            Angle of rotation, where 1 is 90 deg.
        """
        ccw_table = {
            AbsoluteFacing.PosX: AbsoluteFacing.PosZ,
            AbsoluteFacing.NegX: AbsoluteFacing.NegZ,
            AbsoluteFacing.NegY: AbsoluteFacing.NegY,
            AbsoluteFacing.PosY: AbsoluteFacing.PosY,
            AbsoluteFacing.PosZ: AbsoluteFacing.NegX,
            AbsoluteFacing.NegZ: AbsoluteFacing.PosX,
        }
        face = self
        for i in range(angle%4):
            face = ccw_table[face]
        return face

    def rotate_cw(self, angle: int = 1):
        """Rotating the direction clockwise. 
        
        Arg:
            Angle of rotation, where 1 is 90 deg.
        """
        cw_table = {
            AbsoluteFacing.PosX: AbsoluteFacing.NegZ,
            AbsoluteFacing.NegX: AbsoluteFacing.PosZ,
            AbsoluteFacing.NegY: AbsoluteFacing.NegY,
            AbsoluteFacing.PosY: AbsoluteFacing.PosY,
            AbsoluteFacing.PosZ: AbsoluteFacing.PosX,
            AbsoluteFacing.NegZ: AbsoluteFacing.NegX,
        }
        face = self
        for i in range(angle%4):
            face = cw_table[face]
        return face
    
    def to_relative(self, dir: BlockFacing):
        return DecalFace(int(self.rotate_ccw(int(dir))))
    
    def to_coordintate(self):
        name_dict = {
            AbsoluteFacing.PosX: ( 1, 0, 0),
            AbsoluteFacing.NegX: (-1, 0, 0),
            AbsoluteFacing.NegY: ( 0,-1, 0),
            AbsoluteFacing.PosY: ( 0, 1, 0),
            AbsoluteFacing.PosZ: ( 0, 0, 1),
            AbsoluteFacing.NegZ: ( 0, 0,-1),
        }
        return name_dict[self]