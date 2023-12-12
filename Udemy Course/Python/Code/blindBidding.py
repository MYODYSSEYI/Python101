from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
ongoing = True
auctionCandidates = {}
while ongoing == True:

    bidder = input("Who is making the bid?\n")
    bidAmount = int(input("How much are you willing to pay?\n$"))
    continueYesNo = input("Are there more bidders?\n[Y]|[N]\n").upper()

    def auctionHouse(bidder, bidAmount):
        clear()
        auctionCandidates[bidder]=bidAmount

    auctionHouse(bidder, bidAmount)

    if continueYesNo == "N":
        ongoing = False
        break
    else:
        continue

winner = ""
highestBid=0
for name in auctionCandidates:
    i = auctionCandidates[name]
    if i > highestBid:
        winner = name
        highestBid = i
    else:
        highestBid = highestBid
        winner = winner

print(f"The winner is {winner} with an amount of ${highestBid} put into it!")
