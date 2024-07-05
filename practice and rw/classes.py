from rw import animal   #rw is rough work file which is subject to changes.
                        # at the time of practicing i made a quick class in rw named animal to revise inheritance
                        # which probably isn't there anymore hence the error.

class human(animal):
    classvar="le class variable"

    def __init__(self,name,height,weight,race,color,IQ):
        self.name = name
        self.height = height
        self.weight = weight
        self.race = race
        self.color = color
        self.IQ = IQ

    def hgt(self):
        if self.height >= 6.0:
            print("bro gets bitches")
        else:
            print("bro indeed and in fact does not get bitches")
        return self

    def stats(self):
        print(f"{self.name}'s height is {self.height}\nTheir weight is {self.weight}"
              f" KGs\nThe race seems to be {self.race}\nAnd the skin color seems to be"
              f" {self.color}\n{self.name} seems to possess an IQ of {self.IQ}")
        return self

bill = human("bill",6.4,74,"chinese","kanye","110")
bill.hgt()
print(human.classvar)
print(bill.classvar)
bill.stats().hgt()