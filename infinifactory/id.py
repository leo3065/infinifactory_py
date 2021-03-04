from enum import IntEnum

class BlockID(IntEnum):
    # Custom puzzle tools
    Immovable = 24
    InputPlatfrom = 7
    InputPlatfromInvisible = 40
    Invisible = 30
    InvisibleConveyer = 120
    LowerBound = 60
    OutputPlatform = 6
    OutputPlatformInvisible = 320
    OutputPlatformOversized = 343
    OutputPlatformOversizedCorner = 344
    StartingLocation = 33

    # Product blocks, mechanical
    AlienDrugContainerEmpty = 110
    AlienDrugContainerFull = 113
    AlienDrugTop = 109
    AlienTerminalBody = 171
    AlienTerminalKeyboard = 94
    AlienTerminalScreen = 95
    AlienTerminalScreenBroken = 62
    AmmoContainer = 61
    BombDetonator = 210
    BombExplosive = 212
    BombSupport = 211
    CannonBack = 74
    CannonFront = 75
    CannonPivot = 73
    ClawHinge = 80
    ClawMilledMetal = 82
    ClawRawMetal = 170
    Connector = 86
    ControlConsoleBody = 304
    ControlConsoleCorner = 305
    ControlConsoleLever = 306
    ControlConsoleScreen = 307
    CrewQuartersBed = 308
    CrewQuatersDesk = 309
    CrewQuatersSink = 310
    DroneBody = 177
    DroneCannon = 179
    DroneCannonDamaged = 180
    DroneCannonDamagedTip = 190
    DroneSensor = 205
    DroneTreads = 93
    ExtrudedMeralHollow = 230
    ExtrudedMetalSolid = 229
    ForkliftMilledMetal = 71
    ForkliftTruster = 175
    LifeSupportBody = 311
    LifeSupportTank = 312
    LifeSupportTop = 313
    LifeSupportValve = 314
    LightBlue = 133
    LightConnector = 176
    LighOrange = 132
    MissileBody = 84
    MissileTruster = 85
    MissileTop = 83
    NavagationComputerModule = 321
    NavagationComputerPower = 322
    NavagationComputerScreen = 315
    PlasmaEngineConnector = 317
    PlasmaEngineFuelTank = 341
    PlasmaEngineHousing = 340
    PlasmaEngineThruster = 334
    RadarModule = 87
    RadarModuleDamaged = 122
    ResistanceShuttleBody = 302
    ResistanceShuttleTank = 301
    ResistanceShuttleThruster = 300
    ResistanceShuttleWindow = 303
    SatelliteBody = 172
    SatelliteBody2 = 204
    SatelliteCannonBack = 202
    SatelliteCannonFront = 201
    SatelliteSolorPanel = 92
    SatelliteThruster = 203
    ShipMissleBody = 335
    ShipMissleHead1 = 337
    ShipMissleHead2 = 338
    ShipMissleThruster = 336
    ShuttleBody = 173
    ShuttleLaser = 181
    ShuttleThruster = 89
    ShuttleThrusterDamaged = 90
    ShuttleThrusterDamagedTip = 191
    ShuttleWindow = 91
    ShuttleWindowDamaged = 235
    SkipDriveAngleBottom = 332
    SkipDriveAngleMiddle = 333
    SkipDriveAngleTop = 331
    SkipDriveCenter = 327
    SkipDriveCrossHorizontal = 329
    SkipDriveCrossVertial = 330
    SkipDriveStraight = 328
    SpaceBuoyBody = 298
    SpaceBuoyLight = 299
    TestZoneBLue = 50
    TestZoneNone = 51
    TestZoneRed = 49
    TrainingBlockAncient1 = 96
    TrainingBLockAncient2 = 97
    TrainingBlockAncient3 = 98
    TrainingBlockHeistRed = 79
    TrainingBlockHeistWhite = 81
    TrainingBlockMothership = 127

    # Product block, organic
    Critter = 65
    CritterPackaged = 66
    TreeBranchAngled = 57
    TreeBranchStraight = 56
    TreeFoilage = 55
    TreeTrunk = 54
    WhaleEye = 100
    WhaleEyePackaged = 101
    WhaleMeat = 102
    WhileMeatPackaged = 103
    WhaleSKin = 104
    WhaleSkinPackaged = 105
    WhaleSpine = 106
    WhaleSpinePackaged = 107

    # Factory blocks, player
    Blocker = 35
    Conduit = 2
    ConveyorDownward = 0
    ConveyorStandard = 1
    CounterDownward = 16
    CounterForward = 15
    Eviscerator = 17
    Laser = 9
    Lifter = 138
    Platform = 18
    Pusher = 4
    RotatorCCW = 25
    RotatorCW = 39
    SensorDownward = 149
    SensorForward = 5
    Toggle = 152
    WelderDownward = 131
    WelderForward = 8

    # Factory blocks, special
    CargoContainer = 45
    CargoContainerDummy = 46
    ConveyorFixed = 42
    FoodPackager = 36
    MillingMachineClaw = 117
    MillingMachineForklift = 88
    MiningSpike = 48
    PainterRed = 114
    PainterWhite = 99
    StamperControlPanel = 115
    StamperSensor = 23
    Teleporter = 199
    TeleporterPillar = 200
    Transceiver = 151
    TreeJusier = 32

    # Environment, overlord mothership
    OverlordMothershipBorderDoubleSided = 236
    OverlordMothershipBorderSimple = 163
    OverlordMothershipBorderSingleSided = 161
    OverlordMothershipCellBorder = 21
    OverlordMothershipCellScreen = 158
    OverlordMothershipCellUtilities = 41
    OverlordMothershipDoor = 136
    OverlordMothershipStairs = 29
    OverlordMothershipWallExterior = 58
    OverlordMothershipWallLower = 29
    OverlordMothershipWallLowerConveyor = 165
    OverlordMothershipWallUpper = 183
    OverlordMothershipWindow = 130

    # Environment, proving grounds
    ProvingGroundsInputFaceplate = 125
    ProvingGroundsStairs = 129
    ProvingGroundsWall = 124
    ProvingGroundsWallConveyor = 27

    # Environment, skydock 19
    Skydock19BorderCorner = 22
    Skydock19BorderSide = 164
    Skydock19Platform = 185
    Skydock19Support = 43
    Skydock19SupportBottom = 157
    Skydock19SupportTop = 44

    # Environment, resource site 526.81
    ResourceSite52681Stairs = 147
    ResourceSite52681Wall = 139

    # Environment, production zone 2
    ProductionZone2CatwalkStairs = 167
    ProductionZone2CatwalkStraight = 150
    ProductionZone2DrainCorner = 146
    ProductionZone2DrainStraight = 142
    ProductionZone2InputFaceplate = 20
    ProductionZone2WallLower = 162
    ProductionZone2WallLowerInputChute = 144
    ProductionZone2WallLowerNoEdge = 148
    ProductionZone2WallUpper = 145
    ProductionZone2WallUpperConveyor = 169
    ProductionZone2Window = 166

    # Environment, resource site 338.11
    RescourseSite33811Stairs = 141
    RescourseSite33811Wall = 168

    # Environment, resource site 902.42
    RescourseSite90242Burrow = 154
    RescourseSite90242Stairs = 153
    RescourseSite90242WallDirt = 143
    RescourseSite90242WallStructure = 26
    RescourseSite90242Window = 108

    # Environment, resistance barracks
    ResistanceBarracksBorderBarracks = 345
    ResistanceBarracksDoor = 70
    ResistanceBarracksDrainCorner = 68
    ResistanceBarracksDrainStraight = 77
    ResistanceBarracksSupport = 76
    ResistanceBarracksTrack = 78
    ResistanceBarracksWallBarracks = 69
    ResistanceBarracksWallHangarLower = 63
    ResistanceBarracksWallHangarOverhang = 64
    ResistanceBarracksWallHangarUpper = 67
    ResistanceBarracksWindow = 194

    # Environment, remote asteroid  fields
    RemoteAsteroidFieldsWall = 72
    RemoteAsteroidFieldsWorklight = 192

    # Environment, overlord bunkers
    OverlordBunkerCatwalkCorner = 215
    OverlordBunkerCatwalkEdge = 217
    OverlordBunkerCatwalkStairs = 216
    OverlordBunkerChair = 218
    OverlordBunkerDoorLarge = 209
    OverlordBunkerDoorSmall = 226
    OverlordBunkerDrainCorner = 227
    OverlordBunkerDrainStraight = 224
    OverlordBunkerSupportBase = 223
    OverlordBunkerSupportHorizontal1 = 220
    OverlordBunkerSupportHorizontal2 = 228
    OverlordBunkerSupportVertical = 221
    OverlordBunkerTableCorner = 207
    OverlordBunkerTableStraight = 208
    OverlordBunkerTeleporterAlien = 193
    OverlordBunkerWallBunkerLower = 222
    OverlordBunkerWallBunkerUpper = 213
    OverlordBunkerWallOfficeLower = 225
    OverlordBunkerWallOfficeUpper = 214

    # Environment, production zone 1
    ProductionZone1Floor = 233
    ProductionZone1InputFaceplate1x1 = 10
    ProductionZone1InputFaceplate1x5 = 11
    ProductionZone1InputFaceplate5x1 = 12
    ProductionZone1InputFaceplate5x5 = 13
    ProductionZone1Stairs = 234
    ProductionZone1WallLower = 232
    ProductionZone1WallUpper = 231

    # Environment, Atropos station
    AtroposStationAccessDoorHallway1 = 286
    AtroposStationAccessDoorHallway2 = 287
    AtroposStationCatwalkPillar1Tall = 323
    AtroposStationCatwalkPillar17Tall = 292
    AtroposStationCatwalkPillar3Tall = 254
    AtroposStationCatwalkPlatformFacing1 = 255
    AtroposStationCatwalkPlatformFacing2 = 293
    AtroposStationCatwalkStairs = 279
    AtroposStationCellingTrack = 280
    AtroposStationElevator = 281
    AtroposStationElevatorFaceplateDouble = 325
    AtroposStationElevatorFaceplateSingle = 324
    AtroposStationElevatorInput = 297
    AtroposStationElevatorPadCorner = 284
    AtroposStationElevatorPadSide = 285
    AtroposStationElevatorTrackFacing1 = 282
    AtroposStationElevatorTrackFacing2 = 294
    AtroposStationElevatorTrackWall = 283
    AtroposStationHangerDoor = 118
    AtroposStationHangerDoorBorderHorizontal = 264
    AtroposStationHangerDoorBorderVertical = 265
    AtroposStationHangerDoorTeeth = 119
    AtroposStationScaffoldCorner = 288
    AtroposStationScaffoldEdge = 289
    AtroposStationScaffoldInner = 290
    AtroposStationScaffoldStructBottom = 295
    AtroposStationScaffoldStructTop = 296
    AtroposStationScaffoldTrack = 291
    AtroposStationSpaceStation = 155
    AtroposStationWallExteriorInner = 156
    AtroposStationWallExteriorOuter = 159
    AtroposStationWallInteriorLower = 277
    AtroposStationWallInteriorLowerExposed = 278
    AtroposStationWallInteriorUpper = 276
    AtroposStationWindow = 346

    def __str__(self):
        table = {
            # Custom puzzle tools
            BlockID.Immovable: 'Immovable',
            BlockID.InputPlatfrom: 'Input Platfrom',
            BlockID.InputPlatfromInvisible: 'InputPlatfrom, Invisible',
            BlockID.Invisible: 'Invisible',
            BlockID.InvisibleConveyer: 'Invisible, Conveyer',
            BlockID.LowerBound: 'Lower Bound',
            BlockID.OutputPlatform: 'Output Platform',
            BlockID.OutputPlatformInvisible: 'Output Platform, Invisible',
            BlockID.OutputPlatformOversized: 'Output Platform, Oversized',
            BlockID.OutputPlatformOversizedCorner: 'Output Platform, Oversized, Corner',
            BlockID.StartingLocation: 'Starting Location',

            # Product blocks, mechanical
            BlockID.AlienDrugContainerEmpty: 'Alien Drug, Container, Empty',
            BlockID.AlienDrugContainerFull: 'Alien Drug, Container, Full',
            BlockID.AlienDrugTop: 'Alien Drug, Top',
            BlockID.AlienTerminalBody: 'Alien Terminal, Body',
            BlockID.AlienTerminalKeyboard: 'Alien Terminal, Keyboard',
            BlockID.AlienTerminalScreen: 'Alien Terminal, Screen',
            BlockID.AlienTerminalScreenBroken: 'Alien Terminal, Screen, Broken',
            BlockID.AmmoContainer: 'Ammo Container',
            BlockID.BombDetonator: 'Bomb, Detonator',
            BlockID.BombExplosive: 'Bomb, Explosive',
            BlockID.BombSupport: 'Bomb, Support',
            BlockID.CannonBack: 'Cannon, Back',
            BlockID.CannonFront: 'Cannon, Front',
            BlockID.CannonPivot: 'Cannon, Pivot',
            BlockID.ClawHinge: 'Claw, Hinge',
            BlockID.ClawMilledMetal: 'Claw, Milled Metal',
            BlockID.ClawRawMetal: 'Claw, Raw Metal',
            BlockID.Connector: 'Connector',
            BlockID.ControlConsoleBody: 'Control Console, Body',
            BlockID.ControlConsoleCorner: 'Control Console, Corner',
            BlockID.ControlConsoleLever: 'Control Console, Lever',
            BlockID.ControlConsoleScreen: 'Control Console, Screen',
            BlockID.CrewQuartersBed: 'Crew Quarters, Bed',
            BlockID.CrewQuatersDesk: 'Crew Quaters, Desk',
            BlockID.CrewQuatersSink: 'Crew Quaters, Sink',
            BlockID.DroneBody: 'Drone, Body',
            BlockID.DroneCannon: 'Drone, Cannon',
            BlockID.DroneCannonDamaged: 'Drone, Cannon, Damaged',
            BlockID.DroneCannonDamagedTip: 'Drone, Cannon, Damaged, Tip',
            BlockID.DroneSensor: 'Drone, Sensor',
            BlockID.DroneTreads: 'Drone, Treads',
            BlockID.ExtrudedMeralHollow: 'Extruded Meral, Hollow',
            BlockID.ExtrudedMetalSolid: 'Extruded Metal, Solid',
            BlockID.ForkliftMilledMetal: 'Forklift, Milled Metal',
            BlockID.ForkliftTruster: 'Forklift, Truster',
            BlockID.LifeSupportBody: 'Life Support, Body',
            BlockID.LifeSupportTank: 'Life Support, Tank',
            BlockID.LifeSupportTop: 'Life Support, Top',
            BlockID.LifeSupportValve: 'Life Support, Valve',
            BlockID.LightBlue: 'Light, Blue',
            BlockID.LightConnector: 'Light, Connector',
            BlockID.LighOrange: 'Ligh, Orange',
            BlockID.MissileBody: 'Missile, Body',
            BlockID.MissileTruster: 'Missile, Truster',
            BlockID.MissileTop: 'Missile, Top',
            BlockID.NavagationComputerModule: 'Navagation Computer, Module',
            BlockID.NavagationComputerPower: 'Navagation Computer, Power',
            BlockID.NavagationComputerScreen: 'Navagation Computer, Screen',
            BlockID.PlasmaEngineConnector: 'Plasma Engine, Connector',
            BlockID.PlasmaEngineFuelTank: 'Plasma Engine, Fuel Tank',
            BlockID.PlasmaEngineHousing: 'Plasma Engine, Housing',
            BlockID.PlasmaEngineThruster: 'Plasma Engine, Thruster',
            BlockID.RadarModule: 'Radar Module',
            BlockID.RadarModuleDamaged: 'Radar Module, Damaged',
            BlockID.ResistanceShuttleBody: 'Resistance Shuttle, Body',
            BlockID.ResistanceShuttleTank: 'Resistance Shuttle, Tank',
            BlockID.ResistanceShuttleThruster: 'Resistance Shuttle, Thruster',
            BlockID.ResistanceShuttleWindow: 'Resistance Shuttle, Window',
            BlockID.SatelliteBody: 'Satellite, Body',
            BlockID.SatelliteBody2: 'Satellite, Body, 2',
            BlockID.SatelliteCannonBack: 'Satellite, Cannon, Back',
            BlockID.SatelliteCannonFront: 'Satellite, Cannon, Front',
            BlockID.SatelliteSolorPanel: 'Satellite, Solor Panel',
            BlockID.SatelliteThruster: 'Satellite, Thruster',
            BlockID.ShipMissleBody: 'Ship Missle, Body',
            BlockID.ShipMissleHead1: 'Ship Missle, Head 1',
            BlockID.ShipMissleHead2: 'Ship Missle, Head 2',
            BlockID.ShipMissleThruster: 'Ship Missle, Thruster',
            BlockID.ShuttleBody: 'Shuttle, Body',
            BlockID.ShuttleLaser: 'Shuttle, Laser',
            BlockID.ShuttleThruster: 'Shuttle, Thruster',
            BlockID.ShuttleThrusterDamaged: 'Shuttle, Thruster, Damaged',
            BlockID.ShuttleThrusterDamagedTip: 'Shuttle, Thruster, Damaged, Tip',
            BlockID.ShuttleWindow: 'Shuttle, Window',
            BlockID.ShuttleWindowDamaged: 'Shuttle, Window, Damaged',
            BlockID.SkipDriveAngleBottom: 'Skip Drive, Angle, Bottom',
            BlockID.SkipDriveAngleMiddle: 'Skip Drive, Angle, Middle',
            BlockID.SkipDriveAngleTop: 'Skip Drive, Angle, Top',
            BlockID.SkipDriveCenter: 'Skip Drive, Center',
            BlockID.SkipDriveCrossHorizontal: 'Skip Drive, Cross, Horizontal',
            BlockID.SkipDriveCrossVertial: 'Skip Drive, Cross, Vertial',
            BlockID.SkipDriveStraight: 'Skip Drive, Straight',
            BlockID.SpaceBuoyBody: 'Space Buoy, Body',
            BlockID.SpaceBuoyLight: 'Space Buoy, Light',
            BlockID.TestZoneBLue: 'Test Zone, BLue',
            BlockID.TestZoneNone: 'Test Zone, None',
            BlockID.TestZoneRed: 'Test Zone, Red',
            BlockID.TrainingBlockAncient1: 'Training Block, Ancient, 1',
            BlockID.TrainingBLockAncient2: 'Training BLock, Ancient, 2',
            BlockID.TrainingBlockAncient3: 'Training Block, Ancient, 3',
            BlockID.TrainingBlockHeistRed: 'Training Block, Heist, Red',
            BlockID.TrainingBlockHeistWhite: 'Training Block, Heist, White',
            BlockID.TrainingBlockMothership: 'Training Block, Mothership',

            # Product block, organic
            BlockID.Critter: 'Critter',
            BlockID.CritterPackaged: 'Critter, Packaged',
            BlockID.TreeBranchAngled: 'Tree, Branch, Angled',
            BlockID.TreeBranchStraight: 'Tree, Branch, Straight',
            BlockID.TreeFoilage: 'Tree, Foilage',
            BlockID.TreeTrunk: 'Tree, Trunk',
            BlockID.WhaleEye: 'Whale, Eye',
            BlockID.WhaleEyePackaged: 'Whale, Eye, Packaged',
            BlockID.WhaleMeat: 'Whale, Meat',
            BlockID.WhileMeatPackaged: 'While, Meat, Packaged',
            BlockID.WhaleSKin: 'Whale, SKin',
            BlockID.WhaleSkinPackaged: 'Whale, Skin, Packaged',
            BlockID.WhaleSpine: 'Whale, Spine',
            BlockID.WhaleSpinePackaged: 'Whale, Spine, Packaged',

            # Factory blocks, player
            BlockID.Blocker: 'Blocker',
            BlockID.Conduit: 'Conduit',
            BlockID.ConveyorDownward: 'Conveyor, Downward',
            BlockID.ConveyorStandard: 'Conveyor, Standard',
            BlockID.CounterDownward: 'Counter, Downward',
            BlockID.CounterForward: 'Counter, Forward',
            BlockID.Eviscerator: 'Eviscerator',
            BlockID.Laser: 'Laser',
            BlockID.Lifter: 'Lifter',
            BlockID.Platform: 'Platform',
            BlockID.Pusher: 'Pusher',
            BlockID.RotatorCCW: 'Rotator (CCW)',
            BlockID.RotatorCW: 'Rotator (CW)',
            BlockID.SensorDownward: 'Sensor, Downward',
            BlockID.SensorForward: 'Sensor, Forward',
            BlockID.Toggle: 'Toggle',
            BlockID.WelderDownward: 'Welder, Downward',
            BlockID.WelderForward: 'Welder, Forward',

            # Factory blocks, special
            BlockID.CargoContainer: 'Cargo Container',
            BlockID.CargoContainerDummy: 'Cargo Container, Dummy',
            BlockID.ConveyorFixed: 'Conveyor, Fixed',
            BlockID.FoodPackager: 'Food Packager',
            BlockID.MillingMachineClaw: 'Milling Machine, Claw',
            BlockID.MillingMachineForklift: 'Milling Machine, Forklift',
            BlockID.MiningSpike: 'Mining Spike',
            BlockID.PainterRed: 'Painter, Red',
            BlockID.PainterWhite: 'Painter, White',
            BlockID.StamperControlPanel: 'Stamper, Control Panel',
            BlockID.StamperSensor: 'Stamper, Sensor',
            BlockID.Teleporter: 'Teleporter',
            BlockID.TeleporterPillar: 'Teleporter Pillar',
            BlockID.Transceiver: 'Transceiver',
            BlockID.TreeJusier: 'Tree Jusier',

            # Environment, overlord mothership
            BlockID.OverlordMothershipBorderDoubleSided: 'Overlord Mothership, Border, Double-Sided',
            BlockID.OverlordMothershipBorderSimple: 'Overlord Mothership, Border, Simple',
            BlockID.OverlordMothershipBorderSingleSided: 'Overlord Mothership, Border, Single-Sided',
            BlockID.OverlordMothershipCellBorder: 'Overlord Mothership, Cell Border',
            BlockID.OverlordMothershipCellScreen: 'Overlord Mothership, Cell Screen',
            BlockID.OverlordMothershipCellUtilities: 'Overlord Mothership, Cell Utilities',
            BlockID.OverlordMothershipDoor: 'Overlord Mothership, Door',
            BlockID.OverlordMothershipStairs: 'Overlord Mothership, Stairs',
            BlockID.OverlordMothershipWallExterior: 'Overlord Mothership, Wall, Exterior',
            BlockID.OverlordMothershipWallLower: 'Overlord Mothership, Wall, Lower',
            BlockID.OverlordMothershipWallLowerConveyor: 'Overlord Mothership, Wall, Lower, Conveyor',
            BlockID.OverlordMothershipWallUpper: 'Overlord Mothership, Wall, Upper',
            BlockID.OverlordMothershipWindow: 'Overlord Mothership, Window',

            # Environment, proving grounds
            BlockID.ProvingGroundsInputFaceplate: 'Proving Grounds, Input Faceplate',
            BlockID.ProvingGroundsStairs: 'Proving Grounds, Stairs',
            BlockID.ProvingGroundsWall: 'Proving Grounds, Wall',
            BlockID.ProvingGroundsWallConveyor: 'Proving Grounds, Wall, Conveyor',

            # Environment, skydock 19
            BlockID.Skydock19BorderCorner: 'Skydock 19, Border, Corner',
            BlockID.Skydock19BorderSide: 'Skydock 19, Border, Side',
            BlockID.Skydock19Platform: 'Skydock 19, Platform',
            BlockID.Skydock19Support: 'Skydock 19, Support',
            BlockID.Skydock19SupportBottom: 'Skydock 19, Support, Bottom',
            BlockID.Skydock19SupportTop: 'Skydock 19, Support, Top',

            # Environment, resource site 526.81
            BlockID.ResourceSite52681Stairs: 'Resource Site 526.81 Stairs',
            BlockID.ResourceSite52681Wall: 'Resource Site 526.81 Wall',

            # Environment, production zone 2
            BlockID.ProductionZone2CatwalkStairs: 'Production Zone 2, Catwalk, Stairs',
            BlockID.ProductionZone2CatwalkStraight: 'Production Zone 2, Catwalk, Straight',
            BlockID.ProductionZone2DrainCorner: 'Production Zone 2, Drain, Corner',
            BlockID.ProductionZone2DrainStraight: 'Production Zone 2, Drain, Straight',
            BlockID.ProductionZone2InputFaceplate: 'Production Zone 2, Input Faceplate',
            BlockID.ProductionZone2WallLower: 'Production Zone 2, Wall, Lower',
            BlockID.ProductionZone2WallLowerInputChute: 'Production Zone 2, Wall, Lower Input Chute',
            BlockID.ProductionZone2WallLowerNoEdge: 'Production Zone 2, Wall, Lower, No Edge',
            BlockID.ProductionZone2WallUpper: 'Production Zone 2, Wall, Upper',
            BlockID.ProductionZone2WallUpperConveyor: 'Production Zone 2, Wall, Upper, Conveyor',
            BlockID.ProductionZone2Window: 'Production Zone 2, Window',

            # Environment, resource site 338.11
            BlockID.RescourseSite33811Stairs: 'Rescourse Site 338.11, Stairs',
            BlockID.RescourseSite33811Wall: 'Rescourse Site 338.11, Wall',

            # Environment, resource site 902.42
            BlockID.RescourseSite90242Burrow: 'Rescourse Site 902.42, Burrow',
            BlockID.RescourseSite90242Stairs: 'Rescourse Site 902.42, Stairs',
            BlockID.RescourseSite90242WallDirt: 'Rescourse Site 902.42, Wall, Dirt',
            BlockID.RescourseSite90242WallStructure: 'Rescourse Site 902.42, Wall, Structure',
            BlockID.RescourseSite90242Window: 'Rescourse Site 902.42, Window',

            # Environment, resistance barracks
            BlockID.ResistanceBarracksBorderBarracks: 'Resistance Barracks, Border, Barracks',
            BlockID.ResistanceBarracksDoor: 'Resistance Barracks, Door',
            BlockID.ResistanceBarracksDrainCorner: 'Resistance Barracks, Drain, Corner',
            BlockID.ResistanceBarracksDrainStraight: 'Resistance Barracks, Drain, Straight',
            BlockID.ResistanceBarracksSupport: 'Resistance Barracks, Support',
            BlockID.ResistanceBarracksTrack: 'Resistance Barracks, Track',
            BlockID.ResistanceBarracksWallBarracks: 'Resistance Barracks, Wall, Barracks',
            BlockID.ResistanceBarracksWallHangarLower: 'Resistance Barracks, Wall, Hangar, Lower',
            BlockID.ResistanceBarracksWallHangarOverhang: 'Resistance Barracks, Wall ,Hangar, Overhang',
            BlockID.ResistanceBarracksWallHangarUpper: 'Resistance Barracks, Wall, Hangar, Upper',
            BlockID.ResistanceBarracksWindow: 'Resistance Barracks, Window',

            # Environment, remote asteroid fields
            BlockID.RemoteAsteroidFieldsWall: 'Remote Asteroid Fields, Wall',
            BlockID.RemoteAsteroidFieldsWorklight: 'Remote Asteroid Fields, Worklight',

            # Environment, overlord bunkers
            BlockID.OverlordBunkerCatwalkCorner: 'Overlord Bunker, Catwalk, Corner',
            BlockID.OverlordBunkerCatwalkEdge: 'Overlord Bunker, Catwalk, Edge',
            BlockID.OverlordBunkerCatwalkStairs: 'Overlord Bunker, Catwalk, Stairs',
            BlockID.OverlordBunkerChair: 'Overlord Bunker, Chair',
            BlockID.OverlordBunkerDoorLarge: 'Overlord Bunker, Door, Large',
            BlockID.OverlordBunkerDoorSmall: 'Overlord Bunker, Door, Small',
            BlockID.OverlordBunkerDrainCorner: 'Overlord Bunker, Drain, Corner',
            BlockID.OverlordBunkerDrainStraight: 'Overlord Bunker, Drain, Straight',
            BlockID.OverlordBunkerSupportBase: 'Overlord Bunker, Support, Base',
            BlockID.OverlordBunkerSupportHorizontal1: 'Overlord Bunker, Support, Horizontal, 1',
            BlockID.OverlordBunkerSupportHorizontal2: 'Overlord Bunker, Support, Horizontal, 2',
            BlockID.OverlordBunkerSupportVertical: 'Overlord Bunker, Support, Vertical',
            BlockID.OverlordBunkerTableCorner: 'Overlord Bunker, Table, Corner',
            BlockID.OverlordBunkerTableStraight: 'Overlord Bunker, Table, Straight',
            BlockID.OverlordBunkerTeleporterAlien: 'Overlord Bunker, Teleporter, Alien',
            BlockID.OverlordBunkerWallBunkerLower: 'Overlord Bunker, Wall, Bunker, Lower',
            BlockID.OverlordBunkerWallBunkerUpper: 'Overlord Bunker, Wall, Bunker, Upper',
            BlockID.OverlordBunkerWallOfficeLower: 'Overlord Bunker, Wall, Office, Lower',
            BlockID.OverlordBunkerWallOfficeUpper: 'Overlord Bunker, Wall, Office, Upper',

            # Environment, production zone 1
            BlockID.ProductionZone1Floor: 'Production Zone 1, Floor',
            BlockID.ProductionZone1InputFaceplate1x1: 'Production Zone 1, Input Faceplate, 1x1',
            BlockID.ProductionZone1InputFaceplate1x5: 'Production Zone 1, Input Faceplate, 1x5',
            BlockID.ProductionZone1InputFaceplate5x1: 'Production Zone 1, Input Faceplate, 5x1',
            BlockID.ProductionZone1InputFaceplate5x5: 'Production Zone 1, Input Faceplate, 5x5',
            BlockID.ProductionZone1Stairs: 'Production Zone 1, Stairs',
            BlockID.ProductionZone1WallLower: 'Production Zone 1, Wall, Lower',
            BlockID.ProductionZone1WallUpper: 'Production Zone 1, Wall, Upper',

            # Environment, Atropos station
            BlockID.AtroposStationAccessDoorHallway1: 'Atropos Station, Access Door, Hallway 1',
            BlockID.AtroposStationAccessDoorHallway2: 'Atropos Station, Access Door, Hallway 2',
            BlockID.AtroposStationCatwalkPillar1Tall: 'Atropos Station, Catwalk, Pillar, 1 Tall',
            BlockID.AtroposStationCatwalkPillar17Tall: 'Atropos Station, Catwalk, Pillar, 17 Tall',
            BlockID.AtroposStationCatwalkPillar3Tall: 'Atropos Station, Catwalk, Pillar, 3 Tall',
            BlockID.AtroposStationCatwalkPlatformFacing1: 'Atropos Station, Catwalk, Platform, Facing 1',
            BlockID.AtroposStationCatwalkPlatformFacing2: 'Atropos Station, Catwalk, Platform, Facing 2',
            BlockID.AtroposStationCatwalkStairs: 'Atropos Station, Catwalk, Stairs',
            BlockID.AtroposStationCellingTrack: 'Atropos Station, Celling Track',
            BlockID.AtroposStationElevator: 'Atropos Station, Elevator',
            BlockID.AtroposStationElevatorFaceplateDouble: 'Atropos Station, Elevator Faceplate, Double',
            BlockID.AtroposStationElevatorFaceplateSingle: 'Atropos Station, Elevator Faceplate, Single',
            BlockID.AtroposStationElevatorInput: 'Atropos Station, Elevator Input',
            BlockID.AtroposStationElevatorPadCorner: 'Atropos Station, Elevator Pad, Corner',
            BlockID.AtroposStationElevatorPadSide: 'Atropos Station, Elevator Pad, Side',
            BlockID.AtroposStationElevatorTrackFacing1: 'Atropos Station, Elevator Track, Facing 1',
            BlockID.AtroposStationElevatorTrackFacing2: 'Atropos Station, Elevator Track, Facing 2',
            BlockID.AtroposStationElevatorTrackWall: 'Atropos Station, Elevator Track, Wall',
            BlockID.AtroposStationHangerDoor: 'Atropos Station, Hanger Door',
            BlockID.AtroposStationHangerDoorBorderHorizontal: 'Atropos Station, Hanger Door, Border, Horizontal',
            BlockID.AtroposStationHangerDoorBorderVertical: 'Atropos Station, Hanger Door, Border, Vertical',
            BlockID.AtroposStationHangerDoorTeeth: 'Atropos Station, Hanger Door, Teeth',
            BlockID.AtroposStationScaffoldCorner: 'Atropos Station, Scaffold, Corner',
            BlockID.AtroposStationScaffoldEdge: 'Atropos Station, Scaffold, Edge',
            BlockID.AtroposStationScaffoldInner: 'Atropos Station, Scaffold, Inner',
            BlockID.AtroposStationScaffoldStructBottom: 'Atropos Station, Scaffold, Struct, Bottom',
            BlockID.AtroposStationScaffoldStructTop: 'Atropos Station, Scaffold, Struct, Top',
            BlockID.AtroposStationScaffoldTrack: 'Atropos Station, Scaffold, Track',
            BlockID.AtroposStationSpaceStation: 'Atropos Station, Space Station',
            BlockID.AtroposStationWallExteriorInner: 'Atropos Station, Wall, Exterior, Inner',
            BlockID.AtroposStationWallExteriorOuter: 'Atropos Station, Wall, Exterior, Outer',
            BlockID.AtroposStationWallInteriorLower: 'Atropos Station, Wall, Interior, Lower',
            BlockID.AtroposStationWallInteriorLowerExposed: 'Atropos Station, Wall, Interior, Lower, Exposed',
            BlockID.AtroposStationWallInteriorUpper: 'Atropos Station, Wall, Interior, Upper',
            BlockID.AtroposStationWindow: 'Atropos Station, Window',
        }
        return table[self]


class DecalID(IntEnum):
    # Product block, organic
    WhaleEye = 60

    # Factory blocks, special
    PainterRed = 7
    PainterWhite = 8
    StamperControlPanel = 1
    StamperSensor = 20

    # Environment, overlord mothership
    OverlordMothershipLightMedium = 45
    OverlordMothershipLightMediumOff = 49
    OverlordMothershipLightSmall = 46

    # Environment, production zone 2
    ProductionZone2AlienText = 3
    ProductionZone2LightMedium = 4

    # Environment, overlord bunkers
    OverlordBunkerAlienTextLarge1 = 64
    OverlordBunkerAlienTextLarge2 = 65
    OverlordBunkerAlienTextLarge3 = 66
    OverlordBunkerAlienTextSmall = 67
    OverlordBunkerAlienTextSmallOffCenter = 68
    OverlordBunkerLightCool = 62
    OverlordBunkerLightWarm = 61

    # Environment, production zone 1
    ProductionZone1AlienText = 6

    # Environment, Atropos station
    AtroposStationHangerDoorFieldLarge = 17
    AtroposStationHangerDoorFieldSmall = 23
    AtroposStationLightExterior = 9
    AtroposStationLightHallway = 10
    AtroposStationTextBayA = 31
    AtroposStationTextBayB = 32
    AtroposStationTextBayC = 33
    AtroposStationTextBayD = 34
    AtroposStationTextCaution = 15
    AtroposStationTextDanger = 18
    AtroposStationTextDockingStation2 = 14
    AtroposStationTextHanger12 = 12
    AtroposStationTextHanger5 = 12
    AtroposStationTextHanger9 = 13
    AtroposStationTextNotice = 22

    def __str__(self):
        table = {
            # Product block, organic
            DecalID.WhaleEye: 'Whale Eye, Decal',

            # Factory blocks, special
            DecalID.PainterRed: 'Painter, Red, Decal',
            DecalID.PainterWhite: 'Painter, White, Decal',
            DecalID.StamperControlPanel: 'Stamper, Control Panel, Decal',
            DecalID.StamperSensor: 'Stamper, Sensor, Decal',

            # Environment, overlord mothership
            DecalID.OverlordMothershipLightMedium: 'Overlord Mothership, Light, Medium',
            DecalID.OverlordMothershipLightMediumOff: 'Overlord Mothership, Light, Medium, Off',
            DecalID.OverlordMothershipLightSmall: 'Overlord Mothership, Light, Small',

            # Environment, production zone 2
            DecalID.ProductionZone2AlienText: 'Production Zone 2, Alien Text',
            DecalID.ProductionZone2LightMedium: 'Production Zone 2, Light, Medium',

            # Environment, overlord bunkers
            DecalID.OverlordBunkerAlienTextLarge1: 'Overlord Bunker, Alien Text, Large 1',
            DecalID.OverlordBunkerAlienTextLarge2: 'Overlord Bunker, Alien Text, Large 2',
            DecalID.OverlordBunkerAlienTextLarge3: 'Overlord Bunker, Alien Text, Large 3',
            DecalID.OverlordBunkerAlienTextSmall: 'Overlord Bunker, Alien Text, Small',
            DecalID.OverlordBunkerAlienTextSmallOffCenter: 'Overlord Bunker, Alien Text, Small, Off-Center',
            DecalID.OverlordBunkerLightCool: 'Overlord Bunker, Light, Cool',
            DecalID.OverlordBunkerLightWarm: 'Overlord Bunker, Light, Warm',

            # Environment, production zone 1
            DecalID.ProductionZone1AlienText: 'Production Zone 1, Alien Text',

            # Environment, Atropos station
            DecalID.AtroposStationHangerDoorFieldLarge: 'Atropos Station, Hanger Door, Field, Large',
            DecalID.AtroposStationHangerDoorFieldSmall: 'Atropos Station, Hanger Door, Field, Small',
            DecalID.AtroposStationLightExterior: 'Atropos Station, Light, Exterior',
            DecalID.AtroposStationLightHallway: 'Atropos Station, Light, Hallway',
            DecalID.AtroposStationTextBayA: 'Atropos Station, Text, Bay A',
            DecalID.AtroposStationTextBayB: 'Atropos Station, Text, Bay B',
            DecalID.AtroposStationTextBayC: 'Atropos Station, Text, Bay C',
            DecalID.AtroposStationTextBayD: 'Atropos Station, Text, Bay D',
            DecalID.AtroposStationTextCaution: 'Atropos Station, Text, Caution',
            DecalID.AtroposStationTextDanger: 'Atropos Station, Text, Danger',
            DecalID.AtroposStationTextDockingStation2: 'Atropos Station, Text, Docking Station 2',
            DecalID.AtroposStationTextHanger12: 'Atropos Station, Text, Hanger 12',
            DecalID.AtroposStationTextHanger5: 'Atropos Station, Text, Hanger 5',
            DecalID.AtroposStationTextHanger9: 'Atropos Station, Text, Hanger 9',
            DecalID.AtroposStationTextNotice: 'Atropos Station, Text, Notice',
        }
        return table[self]
