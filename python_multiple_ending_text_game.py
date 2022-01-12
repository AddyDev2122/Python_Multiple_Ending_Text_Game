import time 

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

smartphone = 0
laptop = 0

required = ("\nUse only A, B, or C\n") 

def intro():
  print ("After yet another mask and vax mandate, you awaken the "
  "next morning in a thick mental fog. Head spinning and " 
  "fighting the urge to suffocate, however you stand and marvel at your new, "
  "yet welcome moment of clarity. The peace quickly fades when you hear "
  "the grotesque sound of the fake news media. A shady big pharma politician is "
  "running towards you to give you the jab. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the politician
  B. Lie down and wait to be vaccinated
  C. Run""")
  choice = input(">>> ") 
  if choice in answer_A:
    option_rock()
  elif choice in answer_B:
    print ("\nWelp, that was quick. "
    "\n\nYou are vaccinated!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_rock(): 
  print ("\nThe politician is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  A. Run
  B. Throw another rock
  C. Run to a nearby super coder safe haven""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decided to throw another rock, as if the first " 
    "rock thrown did much damage. The rock flew well over the "
    "politicians head. You missed. \n\nYou are vaccinated!")
  elif choice in answer_C:
    option_safe_haven()
  else:
    print (required)
    option_rock()

def option_safe_haven():
  print ("\nYou were hesitant,the safe haven is unprotected. "
  "Before you fully enter, you notice a shiny smartphone on "
  "the ground. Do you pick up the smartphone. Y/N?")
  choice = input(">>> ")
  if choice in yes:
    smartphone = 1 
  else:
    smartphone = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  A. Hide in silence
  B. Fight
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nReally? You're going to hide in the dark? I think "
    "the politician will sniff you out in the dark, right? Not sure, but "
    "I'm going with YES, so...\n\nYou are vaccinated!")
  elif choice in answer_B:
   if smartphone > 0:
    print ("\nYou laid in wait. The shimmering smartphone attracted "
    "the politician, who thought you were no match. As he walked "
    "closer and closer, your heart beat rapidly. As the politician "
    "reached out to grab the smartphone, you coded your way "
    "to safety. \n\nYou survived!")
   else: 
     print ("\nYou should have picked up that smartphone. You're "
     "defenseless. \n\nYou are vaccinated!")
  elif choice in answer_C:
    print ("As the politician enters the safe haven, you sliently "
    "sneak out. You're several feet away, but the politician turns "
    "around and sees you running.")
    option_run()
  else:
    print (required)
    option_safe_haven()

def option_run():
  print ("\nYou run as quickly as possible, but the politician's "
  "speed is too great. You will:")
  time.sleep(1)
  print ("""  A. Hide behind a boulder
  B. Trapped, so you fight
  C. Run towards a super coder city""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("You're easily spotted. "
    "\n\nYour vaccinated!")
  elif choice in answer_B:
    print ("\nYou're no match for a politician. "
    "\n\nYou are vaccinated!")
  elif choice in answer_C:
    option_city()
  else:
    print (required)
    option_run()

def option_city():
  print ("\nWhile frantically running, you notice a "
  "smartphone lying in the mud. You quickly reach down and grab it, "
  "but miss. You try to calm your heavy breathing as you hide "
  "behind a delapitated building, waiting for the politician to come "
  "charging around the corner. You notice a laptop "
  "near your foot. Do you pick it up? Y/N")
  choice = input(">>> ")
  if choice in yes:
    laptop = 1 
  else:
    laptop = 0
  print ("You hear his heavy footsteps and ready yourself for "
  "the impending politician.")
  time.sleep(1)
  if laptop > 0:
    print ("\nYou quickly hold out the laptop and begin coding, "
    "hoping it will stop the politician in time. It does! The politician was a robot "
    "\n\nThis got weird, but you survived!")
  else: 
     print ("\nMaybe you should have picked up the laptop. "
     "\n\nYou are vaccinated!")

intro()
