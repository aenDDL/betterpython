import string
import random
from dataclasses import dataclass, field
from typing import Callable


def generate_uid(lenght: int = 8) -> str:
    return ''.join(random.choices(string.ascii_uppercase, k=lenght))


@dataclass(kw_only=True, frozen=True, slots=True)
class Ticket:
    uid: str = field(default_factory=generate_uid)
    customer: str
    issue: str

    def __str__(self) -> str:
        return f"Processed {self.uid} ticket from {self.customer} with following issue: {self.issue}"


sort_fn = Callable[[list[Ticket]], list[Ticket]]

def sort_normal(tickets: list[Ticket]) -> list[Ticket]:
    return tickets[:]

def sort_reverse(tickets: list[Ticket]) -> list[Ticket]:
    return tickets[::-1]

def sort_blackhole(_: list[Ticket]) -> list[Ticket]:
    return []


@dataclass
class Support:
    tickets: list[Ticket] = field(default_factory=list)
    
    def add_ticket(self, customer: str, issue: str) -> None:
        ticket = Ticket(customer=customer, issue=issue)
        self.tickets.append(ticket)
    
    def process_support(self, method: sort_fn) -> None:
        tickets = method(self.tickets)

        if len(tickets) == 0:
            print("No tickets to process: free day!")
        for ticket in tickets:
            print(ticket)


def main() -> None:
    support = Support()
    support.add_ticket("alan", "teams not working")
    support.add_ticket("alan", "keyboard got destroyed")
    
    for method in [sort_normal, sort_reverse, sort_blackhole]:
        support.process_support(method)
        print('-'* 40)


if __name__ == "__main__":
    main()