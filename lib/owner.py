class Owner:
  def __init__(self, name):
    self.name = name
    self.pets = []

  def adopt_pet(self, pet):
    pet.owner = self
    self.pets.append(pet)


  def __repr__(self):
    return f'<Owner name={self.name}>'
