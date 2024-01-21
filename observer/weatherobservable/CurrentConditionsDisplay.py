from DisplayElement import DisplayElement
from Observable import Observable
from Observer import Observer
from WeatherData import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    observable: Observable
    __temperature: float 
    __humidity: float
        
    def __init__(self, observable: Observable):
        # Our constructor now takes an Observable and we use this to add the current conditions object as an Observer.
        self.observable = observable
        self.observable.addObserver(self)
        
    def update(self, obs: Observable, arg: object):
        # We’ve changed the update() method to take both an Observable and the optional data argument.
        if isinstance(obs, WeatherData):
            weatherData: WeatherData = obs
            # pull happening here. If 'arg' was used instead, it would have been push from Subject's side
            self.__temperature = weatherData.getTemperature() 
            self.__humidity = weatherData.getHumidity()
            self.display()
            
    def display(self) -> None:
        print(f"Current conditions: {self.__temperature}F degrees and {self.__humidity}% humidity")
