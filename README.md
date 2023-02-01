# Luckydraw
This is a lucky draw smart contract written in smartpy language.

The contract Lottery has the following attributes:

admin: an address representing the administrator of the lottery.

participants: a list of addresses representing the participants of the lottery.

prize: the amount of tokens (in this case, tez) that the winner will receive.

winner: an address representing the winner of the lottery.

It has four entry points, which are functions that can be called by a user to interact with the contract:

participate: allows a user to participate in the lottery if they are not already in the list of participants.

draw: allows the admin to draw a winner from the list of participants, if there are exactly three participants.

claim_prize: allows the winner to claim their prize by sending the tokens to their address.

selfdestruct: ends the contract when the prize has been claimed.

The test function sets up a test scenario for the contract, using the sp.test_scenario method.
It creates an instance of the contract, adding participants, and then drawing a winner. 
The test scenario verifies that a winner has been chosen, and then triggers the claim_prize function to end the contract.

Finally, the sp.add_compilation_target method compiles the contract and its associated test function and gives it the name Lottery_comp.


