class Move:
    def __init__(
        self,
        id,
        name,
        power,
        pp,
        priority,
        type
    ):
        self._id = id,
        self._name = name,
        self._power = power,
        self._pp = pp,
        self._priority = priority
        self._type = type

    def get_All_Moves():
        pass
    
    # Getters
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def power(self):
        return self._power

    @property
    def pp(self):
        return self._pp

    @property
    def priority(self):
        return self._priority

    @property
    def type(self):
        return self._type

    # Setters
    @id.setter
    def id(self, value):
        self._id = value

    @name.setter
    def name(self, value):
        self._name = value

    @power.setter
    def power(self, value):
        self._power = value

    @pp.setter
    def pp(self, value):
        self._pp = value

    @priority.setter
    def priority(self, value):
        self._priority = value

    @type.setter
    def type(self, value):
        self._type = value

    # __str__
    def __str__(self):
        return (
            f"Move(id={self._id}, name={self._name}, power={self._power}, "
            f"pp={self._pp}, priority={self._priority}, type={self._type})"
        )