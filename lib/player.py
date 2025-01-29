from actor import Actor

class Player(Actor):
  def __init__(self, name, stats, controls):
    super().__init__(name=name, stats=stats)
    self.controls = controls

  def attack(self, other):
    super().attack(other)
    print('heals from the enchanted bam stick')