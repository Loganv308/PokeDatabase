class Pokemon:
    def __init__(
        self,
        id,
        name,
        height,
        weight,
        hp_base,
        attack_base,
        defense_base,
        spec_attack_base,
        spec_defense_base,
        speed_base,
    ):
        self._id = id
        self._name = name
        self._height = height
        self._weight = weight
        self._hp_base = hp_base
        self._attack_base = attack_base
        self._defense_base = defense_base
        self._spec_attack_base = spec_attack_base
        self._spec_defense_base = spec_defense_base
        self._speed_base = speed_base
    
    def __str__(self):
        return f"{self.name} ID: {self.id} | "

    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    # height
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # hp_base
    @property
    def hp_base(self):
        return self._hp_base

    @hp_base.setter
    def hp_base(self, value):
        self._hp_base = value

    # attack_base
    @property
    def attack_base(self):
        return self._attack_base

    @attack_base.setter
    def attack_base(self, value):
        self._attack_base = value

    # defense_base
    @property
    def defense_base(self):
        return self._defense_base

    @defense_base.setter
    def defense_base(self, value):
        self._defense_base = value

    # spec_attack_base
    @property
    def spec_attack_base(self):
        return self._spec_attack_base

    @spec_attack_base.setter
    def spec_attack_base(self, value):
        self._spec_attack_base = value

    # spec_defense_base
    @property
    def spec_defense_base(self):
        return self._spec_defense_base

    @spec_defense_base.setter
    def spec_defense_base(self, value):
        self._spec_defense_base = value

    # speed_base
    @property
    def speed_base(self):
        return self._speed_base

    @speed_base.setter
    def speed_base(self, value):
        self._speed_base = value