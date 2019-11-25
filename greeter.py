while True:
  print('What is your name? (Enter \'quit\' or \'exit\' to exit)')
  userInput = input()
  if userInput == 'quit' or userInput == 'exit':
    exit(0)
  print('Hello, ' + userInput)