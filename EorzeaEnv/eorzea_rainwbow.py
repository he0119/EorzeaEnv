from collections import deque
from dataclasses import dataclass
from typing import Union

from EorzeaEnv.eorzea_place_name import EorzeaPlaceName
from EorzeaEnv.eorzea_time import EorzeaTime

from .Data.TerritoryWeather import territory_weather as _territory_weather
from .Data.WeatherRate import weather_rate as _weather_rate

RAINY_WEATHERS = {7, 8, 10}


@dataclass
class WeatherInfo:
    time: EorzeaTime
    raw_weather: int


class EorzeaRainbow:
    _weather_slot: deque[WeatherInfo]
    _is_possible: bool
    _place_name: EorzeaPlaceName

    def __init__(self, place_name: EorzeaPlaceName) -> None:
        self._place_name = place_name
        self._weather_slot = deque([], maxlen=2)
        self._is_possible = _is_rainbow_possible(place_name)

    @property
    def place_name(self):
        return self._place_name

    @property
    def is_appear(self):
        if len(self._weather_slot) == 2 and self._is_possible:
            prev_weather, current_weather = self._weather_slot
            if _check_sun(current_weather.time.sun):
                time_ticket = current_weather.time.hour*100 + current_weather.time.minute
                if 600 <= time_ticket <= 1800:
                    return all((
                        prev_weather.raw_weather in RAINY_WEATHERS,
                        current_weather.raw_weather not in RAINY_WEATHERS
                    ))
        return False

    def append(self, timestamp: Union[int, float], raw_weather: int):
        self._weather_slot.append(
            WeatherInfo(
                time=EorzeaTime.from_timestamp(timestamp),
                raw_weather=raw_weather)
        )


def _is_rainbow_possible(place_name: EorzeaPlaceName) -> bool:
    weather_rate_index = _territory_weather[place_name.index]
    weather_rate = _weather_rate[weather_rate_index]
    possible_weathers: set[int] = {
        w[1]
        for w in weather_rate
    }
    return all((possible_weathers - RAINY_WEATHERS, RAINY_WEATHERS & possible_weathers))


def _check_sun(sun: int):
    return sun >= 27 or sun <= 6
