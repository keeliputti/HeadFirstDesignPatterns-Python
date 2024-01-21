from Observable import Observable


class WeatherData(Observable):
    __temperature: float 
    __humidity: float
    __pressure: float
        
    def __init__(self):
        super().__init__()

"""
Notice we aren’t sending a data object with the notifyObservers() call. That means we’re using the PULL model.
"""
    def measurementsChanged(self) -> None:
        self.setChanged()
        self.notifyObservers()
        
    def setMeasurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurementsChanged()
        
    def getTemperature(self) -> float:
        return self.__temperature
    
    def getHumidity(self) -> float:
        return self.__humidity
    
    def getPressure(self) -> float:
        return self.__pressure
