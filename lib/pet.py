class Pet:
  all = []

  def __init__(self, name, age, breed, species):
    self.name = name
    self.age = age
    self.breed = breed
    self.species = species
    Pet.all.append(self)

  def eat(self, food):
    print(f'{self.name} eats {food}!')

  @property
  def owner(self):
    return self._owner
  
  @owner.setter
  def owner(self, owner):
    self._owner = owner
    owner.pets.append(self)

  # def get_adopted(self, owner):
  #   owner.adopt_pet(self)

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if name == "":
      raise Exception("Name must exist")
    self._name = name

  @classmethod
  def inventory(cls):
    inventory_dict = {}
    uniq_species = list(set([pet.species for pet in cls.all]))
    for species in uniq_species:
      inventory_dict[species] = [pet.species for pet in cls.all].count(species)

    for species in inventory_dict.keys():
      print(f'There are {inventory_dict[species]} {species}s.')


  def __repr__(self):
    return f'<Pet name="{self.name}" age={self.age} breed="{self.breed}" species="{self.species}">'
  


'''
Pet Attributes
- name,
- breed,
- species,
- age
'''

