print("This is a program that randomized greeting phrases based on your name, as well as a group of greeting phrases (example: Salutations), and introductions (example: I am). The code randomly generates from these pools, and some names have custom pools, specifically made for those names. Remember: This code is driven by your support. If you have any names that I dont cover in this code, send them over to 'theprimordialcube.animations@gmail.com'.")
print("Do you want to go to the Greetimg maker, or the goodbye maker? Use the same cues as before.")

what_do_you_want = input()

if what_do_you_want == 'greeting':
  import GreetingMaker
if what_do_you_want == 'goodbye':
  import GoodbyeMaker