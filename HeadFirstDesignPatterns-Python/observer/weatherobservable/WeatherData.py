from Observable import Observable


class WeatherData(Observable):
    __temperature: float 
    __humidity: float
    __pressure: float
        
    def __init__(self):
        super().__init__()

# We don’t need to keep track of our observers anymore, or manage their registration and removal, 
# (the superclass will handle that) so we’ve removed the code for register, add and notify.
        
# Notice we aren’t sending a data object with the notifyObservers() call. That means we’re using the PULL model.
    
    def measurementsChanged(self) -> None:
        self.setChanged()
        # We now first call setChanged() to indicate the state has changed before calling notifyObservers().
        self.notifyObservers()
        
    def setMeasurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.measurementsChanged()

# These methods aren’t new, but because we are going to use “pull” we thought we’d remind you they are here. 
# The Observers will use them to get at the WeatherData object’s state.
           
    def getTemperature(self) -> float:
        return self.__temperature
    
    def getHumidity(self) -> float:
        return self.__humidity
    
    def getPressure(self) -> float:
        return self.__pressure
