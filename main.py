#Magic 8 ball
#author: Sehaj

#create a list of 20 random outcomes for python to choose from
x = ("It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Outlook not so good.","Very doubtful.")

#create a while loop to come back to the question if not replied properly
while True:
  y = input("Do you want the Magic 8 ball answer your questions? (yes/no) ")

#use if statements for different input outcomes
  if y == "yes":

#nest a while loop to ask the question again if and when needed
    while True:
      input("Ask your question: ")
      print("Thinking in progress...")
      import random
      a = random.choice(x)
      print("Your answer: " + a)

#nest another while loop to be back to the question when input is not proper
      while True:
        b = input("Do you want to ask a question again? (yes/no) ")

#use if statements for different outputs for respective inputs
        if b == "yes":
          break
        if b == "no":
          break
        else:
          print("Please respond with yes or no and try again.")
          continue

#break the outer while loop again for input "no" to b
      if b == "no":
        print("Thanks for your response!")
        break  
  elif y == "no":
    print("Thanks for your response!")
    break
  else:
    print("Please respond with yes or no and try again.")
    continue

#break the main while loop for input "no" to b
  if b == "no":
    break
