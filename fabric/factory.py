from typing import override

from wall import BrickWall, WoodWall
from roof import TileRoof, WoodRoof
from window import PlasticFrameWindow, WoodFrameWindow

class HouseFactory:
    def createWall(self):
        ...
    
    def createRoof(self):
        ...

    def createWindow(self):
        ...


class StoneHouseFactory(HouseFactory):
    @override
    def createWall(self):
        return BrickWall()
    
    @override
    def createRoof(self):
        return TileRoof()

    @override
    def createWindow(self):
        return PlasticFrameWindow()

class WoodHouseFactory(HouseFactory):
    @override
    def createWall(self):
        return WoodWall()
    
    @override
    def createRoof(self):
        return WoodRoof()

    @override
    def createWindow(self):
        return WoodFrameWindow()