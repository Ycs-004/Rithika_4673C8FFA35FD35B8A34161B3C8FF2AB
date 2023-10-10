'''implement a class called player that represents a cricket player.
the play class should have a method called play() which prints" the player is playing cricket
device two classEdu,batsman and bowler, from the player class.
override the play()method in each derived class to print" the batsman is batting"and"the bowler is bowling", 
respectlovely write a program to create objects of booth the batsman create objects of both the batsman and bowler classes and call the play() method for each objects'''


# defined the base class player
class player:
  def play(self):
    print("the player is playing cricket.")

#define the derived class batsman
class Batsman(player):
  def play(self):
    print("the batsman is batting.")

# defined the derived class bowler
class Bowler(player):
  def play(self):
    print("the bowler is bowling")

# create objects of batsman and bowler classEdu
batsman = Batsman()
bowler = Bowler()

# call the play() method to each object
batsman.play()
bowler.play()

