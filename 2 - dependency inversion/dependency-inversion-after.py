from typing import Protocol
from dataclasses import dataclass, field


class Switchable(Protocol):
    def turn_on(self) -> None: ...

    def turn_off(self) -> None: ...


class Light(Switchable):
    def turn_on(self) -> None:
        print("Light turned on.")
    
    def turn_off(self) -> None:
        print("Light turned off.")


class Fan(Switchable):
    def turn_on(self) -> None:
        print("Fan turned on.")
    
    def turn_off(self) -> None:
        print("Fan turned off.")


@dataclass
class Switch:
    device: Switchable
    is_switched: bool = field(default=False)

    def switch(self) -> None:
        self.device.turn_on() if self.is_switched else self.device.turn_off()
        self.is_switched = not self.is_switched


def main() -> None:
    device = Light()
    switch = Switch(device=device)

    for _ in range(0, 10):
        switch.switch()


if __name__ == "__main__":
    main()