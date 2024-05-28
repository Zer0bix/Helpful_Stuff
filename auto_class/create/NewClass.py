class Car:
    # Attributes
    _name = None
    _character_class = None
    _armor = None
    _level = None
    _experience_points = None
    _hit_points = None
    _armor_class = None
    _skills = None
    _inventory = None
    _gold = None
    _attribute_points = None

    # Initialize
    def __init__(self, name = None, character_class = None, armor = None, level = None, experience_points = None, hit_points = None, armor_class = None, skills = None, inventory = None, gold = None, attribute_points = None):

        self._name = name
        self._character_class = character_class
        self._armor = armor
        self._level = level
        self._experience_points = experience_points
        self._hit_points = hit_points
        self._armor_class = armor_class
        self._skills = skills
        self._inventory = inventory
        self._gold = gold
        self._attribute_points = attribute_points

    # Getters
    def get_name(self):
        return self._name

    def get_character_class(self):
        return self._character_class

    def get_armor(self):
        return self._armor

    def get_level(self):
        return self._level

    def get_experience_points(self):
        return self._experience_points

    def get_hit_points(self):
        return self._hit_points

    def get_armor_class(self):
        return self._armor_class

    def get_skills(self):
        return self._skills

    def get_inventory(self):
        return self._inventory

    def get_gold(self):
        return self._gold

    def get_attribute_points(self):
        return self._attribute_points


    # Mutators
    def set_name(self, name):
        self._name = name

    def set_character_class(self, character_class):
        self._character_class = character_class

    def set_armor(self, armor):
        self._armor = armor

    def set_level(self, level):
        self._level = level

    def set_experience_points(self, experience_points):
        self._experience_points = experience_points

    def set_hit_points(self, hit_points):
        self._hit_points = hit_points

    def set_armor_class(self, armor_class):
        self._armor_class = armor_class

    def set_skills(self, skills):
        self._skills = skills

    def set_inventory(self, inventory):
        self._inventory = inventory

    def set_gold(self, gold):
        self._gold = gold

    def set_attribute_points(self, attribute_points):
        self._attribute_points = attribute_points


