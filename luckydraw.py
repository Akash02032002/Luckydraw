import smartpy as sp

class Lottery(sp.Contract):
  def __init__(self, admin, participants, prize):
    self.init(
      admin = sp.address("admin"),
      participants = participants,
      prize = prize,
      winner = sp.none
    )
  
  @sp.entry_point
  def participate(self, params):
    sp.verify(sp.sender not in self.data.participants)
    self.data.participants.append(sp.sender)
  
  @sp.entry_point
  def draw(self, params):
    sp.verify(sp.sender == self.data.admin)
    sp.verify(len(self.data.participants) == 3)
    self.data.winner = sp.random_choice(self.data.participants)
  
  @sp.entry_point
  def claim_prize(self, params):
    sp.verify(sp.sender == self.data.winner)
    sp.send(sp.sender, self.data.prize)
    sp.terminate(sp.sender)

@sp.add_test(name = "Lottery")
def test():
  scenario = sp.test_scenario()
  contract = Lottery(sp.address("admin"), [], sp.tez(1000))
  scenario += contract
  scenario += contract.participate()
  scenario += contract.participate()
  scenario += contract.participate()
  scenario += contract.draw()
  scenario.verify(contract.data.winner != sp.none)
  scenario += contract.claim_prize()

sp.add_compilation_target("Lottery_comp", Lottery, test)