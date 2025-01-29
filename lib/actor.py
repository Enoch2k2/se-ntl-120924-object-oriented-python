class Actor:
  def __init__(self,  name, stats):
    self.name = name
    self.stats = stats

  def attack(self, other):
    print(f'{self.name} attacks {other.name}!')