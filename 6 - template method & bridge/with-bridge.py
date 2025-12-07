from typing import List, Protocol
from abc import ABC, abstractmethod
from dataclasses import dataclass


class Exchange(Protocol):
    def connect(self) -> None: ...
    def get_prices(self) -> List[float]: ...

class Binance(Exchange):
    def connect(self) -> None:
        print("Connecting to Binance...")

    def get_prices(self) -> List[float]:
        return [10.0, 12.5, 11.0, 13.0, 9.5]

class Bybit(Exchange):
    def connect(self) -> None:
        print("Connecting to Bybit...")

    def get_prices(self) -> List[float]:
        return [11.0, 12.0, 10.5, 14.0, 9.0]


class TradingBot(ABC):
    # TODO: not sure if ABC > Protocol: thing to study for me in the future
    exchange: Exchange

    @abstractmethod
    def sell(self, prices: List[float]) -> bool: ...

    @abstractmethod
    def buy(self, prices: List[float]) -> bool: ...

    def run(self) -> None:
        self.exchange.connect()
        prices = self.exchange.get_prices()

        if self.sell(prices):
            print("Bot decided to SELL")
        elif self.buy(prices):
            print("Bot decided to BUY")
        else:
            print("Bot decided to do nothing")

@dataclass(frozen=True, slots=True)
class MinMaxBot(TradingBot):
    exchange: Exchange 

    def sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)

    def buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

@dataclass(frozen=True, slots=True)
class AvgBot(TradingBot):
    exchange: Exchange

    def _avg(self, prices: List[float]) -> float:
        return sum(prices) / len(prices) if prices else 0.0

    def sell(self, prices: List[float]) -> bool:
        return prices[-1] > self._avg(prices)

    def buy(self, prices: List[float]) -> bool:
        return prices[-1] < self._avg(prices)


def main() -> None:
    bot = MinMaxBot(exchange=Binance())
    bot.run()

if __name__ == "__main__":
    main()