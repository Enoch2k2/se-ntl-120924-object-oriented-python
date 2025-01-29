class Cli:
  def start(self):
    print("Welcome to Pet Shop!")
    self.menu()

  def menu(self):
    print("Type 1-3 or type 'exit' to exit program")
    print("1. To list pets")
    print("2. To create a pet")
    print("3. To Adopt a pet")
    print("exit to exit program")
    self.menu_selection()

  def menu_selection(self):
    user_input = input("Enter 1-3 or exit: ")
    if user_input == "1":
      print("listing pets")    
    elif user_input == "2":
      print("creating pets!")
    elif user_input == "3":
      print("Adopting a pet!")
    elif user_input == "exit":
      print("Exiting program")
      exit()
    self.menu()