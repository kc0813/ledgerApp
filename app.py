# main functionality and logic of the program

""" TODO:   sanitize s before throwing s in this method
            Add code for when a person is not found in a ledger (both reciever and sender)
            refactor ;-;
"""


def owe(s: str, testing=False) -> bool:
    sender, doesOwe, receiver, amt = s.lower().strip().split(" ")

    if doesOwe == "owe":
        # first check if the person lending you money owes you money
        # if they do take away from their existing balance first
        if not testing:
            rledger = open(
                # assumes you are in the ledgerApp directory
                file=r"./ledgers/{0}.txt".format(receiver),
                mode="w+",
            )
        else:
            # we are testing here
            rledger = open(
                # assumes you are in the ledgerApp directory
                file=r"./tests/testRledger.txt",
                mode="w+",
            )
        for line in rledger:
            creditor, amtOwed = line.lower().strip().split(": ")
            # Check if the reciever owes the sender money.
            if creditor == sender:
                if amt <= amtOwed:
                    amtOwed -= amt
                    amt = 0
                elif amt > amtOwed:
                    amtOwed = 0
                    amt -= amtOwed

                willBreak = True

                rledger.write("{}: {}".format(creditor, amtOwed))
                break
        rledger.close()

        # second check if the sender still owes moeny
        # if so, process that
        if amt > 0:
            sledger = open(
                # assumes you are in the ledgerApp directory
                file=r"./tests/testSledger.txt",
                mode="w+",
            )

            for line in sledger:
                creditor, amtOwed = line.lower().strip().split(": ")

                if creditor == receiver:
                    amtOwed += amt
                    sledger.write("{}: {}".format(creditor, amtOwed))
                    break

            sledger.close()


# [name of the person you owe]: amt
# arr = [i for i in range(10)]
