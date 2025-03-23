from typing import override
from .wall import 

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
        ...
    
    @override
    def createRoof(self):
        ...

    @override
    def createWindow(self):
        ...

public class StoneHouseFactory implements HouseFactory {

	@Override
	public Wall createWall() {
		return new BrickWall();
	}

	@Override
	public Roof createRoof() {
		return new TileRoof();
	}

	@Override
	public Window createWindow() {
		return new PlasticFrameWindow();
	}

}