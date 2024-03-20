# region Multiple Assignments
from dataclasses import dataclass
from typing import NamedTuple


def print_vars_01():
    print(f"{a=}")
    print(f"{b=}")
    print(f"{c=}")


a = 1
b = 1
c = 1
print_vars_01()

a = b = c = 1
print_vars_01()

a = b = c = [1, 2, 3]
print_vars_01()


# endregion Multiple Assignments
# region Unpacking
def print_vars_02():
    print(f"{first=}")
    print(f"{others=}")


fruits = ("banana", "apple", "peach")

first = fruits[0]
others = fruits[1:]

print_vars_02()

first, *others = fruits

print_vars_02()

best = "apple"
worst = "banana"

worst, best = best, worst

print(best, worst)


# endregion Unpacking
# region Named Tuples
class Stats(NamedTuple):
    minimum: int
    maximum: int
    count: int
    total: int
    average: float


def get_stats(grades):
    minimum = min(grades)
    maximum = max(grades)
    count = len(grades)
    total = sum(grades)
    average = total / count
    # return minimum, maximum, count, total, average
    return Stats(
        minimum=minimum, maximum=maximum, count=count, total=total, average=average
    )


grades = [55, 42, 33, 100, 88, 78, 98, 4]
minimum, maximum, count, total, average = get_stats(grades=grades)
stats = get_stats(grades=grades)
print(f"{stats.minimum}, {stats.maximum}")
# endregion Named Tuples
# region Virtual environments
"""
python3 -m venv .venv
. .venv/bin/activate
pip install requests
"""


# endregion Virtual environments
# region Built-in Functions
def get_climbers():
    return [
        {"name": "Adam Ondra", "age": 30, "grade": "9c"},
        {"name": "Lucas Viana", "age": 38, "grade": "7a"},
        {"name": "Jakob Schubert", "age": 33, "grade": "9c"},
        {"name": "Alex Megos", "age": 30, "grade": "9b"},
    ]


climbers = get_climbers()
for i in range(len(climbers)):
    print(i, ": ", climbers[i]["name"])

for i, climber in enumerate(climbers):
    print(i, ": ", climber["name"])


# endregion Built-in Functions
# region Dataclasses
@dataclass
class Climber:
    name: str
    age: int
    grade: str


climbers = []
for climber in get_climbers():
    climbers.append(
        Climber(name=climber["name"], age=climber["age"], grade=climber["grade"])
    )

for i, climber in enumerate(climbers):
    print(i, ": ", climber.name)

climbers = [Climber(**climber) for climber in get_climbers()]


for i, climber in enumerate(climbers):
    print(i, ": ", climber.name)


# endregion Dataclasses
# region Sorting
def by_grade(climber):
    return climber.grade


for i, climber in enumerate(sorted(climbers, key=by_grade)):
    print(i, ": ", climber.name, climber.grade)

for i, climber in enumerate(sorted(climbers, key=lambda x: x.grade, reverse=True)):
    print(i, ": ", climber.name, climber.grade)
# endregion Sorting
# region F-string
for i, climber in enumerate(sorted(climbers, key=lambda x: x.grade, reverse=True)):
    print(f"{i} | {climber.name} | {climber.grade}")

for i, climber in enumerate(sorted(climbers, key=lambda x: x.grade, reverse=True)):
    print(f"{i:<2} | {climber.name:<12.12} | {climber.grade:<3}")
# endregion F-string
