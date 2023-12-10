from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

class QueryBuilder:
    def __init__(self) -> None:
        self._matcher = All()

    def build(self):
        matcher = self._matcher
        self._matcher = All()
        return matcher

    def playsIn(self, team):
        self._matcher = And(PlaysIn(team), self._matcher)
        return self

    def hasAtLeast(self, value, attr):
        self._matcher = And(HasAtLeast(value, attr), self._matcher)
        return self

    def hasFewerThan(self, value, attr):
        self._matcher = And(HasFewerThan(value, attr), self._matcher)
        return self

    def invert(self):
        self._matcher = Not(self._matcher)
        return self

    def oneOf(self, *matchers):
        self._matcher = And(Or(*matchers), self._matcher)
        return self
