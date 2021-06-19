choice_message = 'You can choose between the Greeting maker (greeting), and the goodbye maker (goodbye). Type the appropriate phrase to use that specific peice of code (it is CaSE SenSITIvE). If you still dont understand the concept, type (new).'

print("This is the online greeting/goodbye maker. Have a meeting coming up, and dont know what to say? Going to a new place, and need something to pick up the conversation? Need a goodbye phrase to your classmates after graduating colledge? Then you need this program, the online greeting/goodbye maker. Press space, followed by enter to continue.")

proceed_question = input()

if proceed_question ==' ':
  print(choice_message)

what_do_you_want = input()

if what_do_you_want == 'greeting':
  import GreetingMaker
if what_do_you_want == 'goodbye':
  import GoodbyeMaker
if what_do_you_want == 'new':
  import New
