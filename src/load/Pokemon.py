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
    
    # Class instance String
    def __str__(self):
        return f"Name: {self._name} | ID: {self._id} | Height: {self._height} | Weight: {self._weight} | HP: {self._hp_base} | Attack: {self._attack_base} | Defense: {self._defense_base} | Special Attack: {self._spec_attack_base} | Special Defense: {self._spec_defense_base} | Speed: {self._speed_base}"

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
        
    def categorize_stat(self, value: int) -> str:
        if value <= 50:
            return "very low"
        elif value <= 70:
            return "low"
        elif value <= 90:
            return "average"
        elif value <= 110:
            return "high"
        elif value <= 130:
            return "very high"
        else:
            return "elite"

    def calculate_stat(self, base: int, level: int, is_hp=False) -> int:
        if is_hp:
            return int(((2 * base * level) / 100) + level + 10)
        return int(((2 * base * level) / 100) + 5)
    
    def stats_at_level(self, level: int) -> dict:
        return {
            "hp": self.calculate_stat(self.hp_base, level, is_hp=True),
            "attack": self.calculate_stat(self.attack_base, level),
            "defense": self.calculate_stat(self.defense_base, level),
            "spec_attack": self.calculate_stat(self.spec_attack_base, level),
            "spec_defense": self.calculate_stat(self.spec_defense_base, level),
            "speed": self.calculate_stat(self.speed_base, level),
        }
        
    def get_strengths(self) -> list:
        stats = {
            "HP": self.hp_base,
            "Attack": self.attack_base,
            "Defense": self.defense_base,
            "Special Attack": self.spec_attack_base,
            "Special Defense": self.spec_defense_base,
            "Speed": self.speed_base,
        }

        avg = sum(stats.values()) / len(stats)
        return [name for name, value in stats.items() if value >= avg * 1.15]
    
    def get_weaknesses(self) -> list:
        stats = {
            "HP": self.hp_base,
            "Attack": self.attack_base,
            "Defense": self.defense_base,
            "Special Attack": self.spec_attack_base,
            "Special Defense": self.spec_defense_base,
            "Speed": self.speed_base,
        }

        avg = sum(stats.values()) / len(stats)
        return [name for name, value in stats.items() if value <= avg * 0.85]
    
    def get_primary_role(self) -> str:
        ROLE_THRESHOLDS = {
        "physical_sweeper":  {"Attack": 1.2,  "Speed": 1.15},
        "special_sweeper":   {"Special Attack": 1.2, "Speed": 1.15},
        "physical_wall":     {"Defense": 1.2, "HP": 1.1},
        "special_wall":      {"Special Defense": 1.2, "HP": 1.1},
        "tank":              {"HP": 1.25, "Defense": 1.1, "Special Defense": 1.1},
        "wallbreaker":       {"Attack": 1.3, "Special Attack": 1.15},
        "revenge_killer":    {"Speed": 1.3, "Attack": 1.1},
        "support":           {"HP": 1.1, "Defense": 1.05, "Special Defense": 1.05},
        "pivot":             {"Speed": 1.1, "HP": 1.1},
        }

        GLOBAL_STAT_AVERAGES = {
            "HP": 69,
            "Attack": 79,
            "Defense": 73,
            "Special Attack": 72,
            "Special Defense": 71,
            "Speed": 68,
        }
        
        stats = {
            "HP": self.hp_base,
            "Attack": self.attack_base,
            "Defense": self.defense_base,
            "Special Attack": self.spec_attack_base,
            "Special Defense": self.spec_defense_base,
            "Speed": self.speed_base,
        }

        role_scores = {}

        for role, requirements in ROLE_THRESHOLDS.items():
            if all(
                stats[stat] >= GLOBAL_STAT_AVERAGES[stat] * multiplier
                for stat, multiplier in requirements.items()
            ):
                # Score = average % above threshold across all required stats
                score = sum(
                    stats[stat] / (GLOBAL_STAT_AVERAGES[stat] * multiplier)
                    for stat, multiplier in requirements.items()
                ) / len(requirements)
                role_scores[role] = score

        if not role_scores:
            return "balanced"

        return max(role_scores, key=role_scores.get)
    
    def to_document(self) -> str:
        strengths = ", ".join(self.get_strengths()) or "none"
        weaknesses = ", ".join(self.get_weaknesses()) or "none"

        return f"""
            {self.name} (ID: {self.id})

            Base Stats:
            HP: {self.hp_base} ({self.categorize_stat(self.hp_base)})
            Attack: {self.attack_base} ({self.categorize_stat(self.attack_base)})
            Defense: {self.defense_base} ({self.categorize_stat(self.defense_base)})
            Special Attack: {self.spec_attack_base} ({self.categorize_stat(self.spec_attack_base)})
            Special Defense: {self.spec_defense_base} ({self.categorize_stat(self.spec_defense_base)})
            Speed: {self.speed_base} ({self.categorize_stat(self.speed_base)})

            Strengths: {strengths}
            Weaknesses: {weaknesses}
            Battle Role: {self.get_primary_role()}
            """