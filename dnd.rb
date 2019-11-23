#Dungeons & Dragons Dice Roller Script - Created by Patrick M. Howard

$new_line ="--" * 20

class Dnd
  def initialize(die, times)
    @die = die
    @times = times
    @dnd = {"d4" => 4, "d6" => 6, "d10" => 10, "d20" => 20, "d40" => 40}
  end

  def roll_dice()
    i = 0
    while i < @times do
      result = rand(@dnd[@die])
      result > 0? puts("#{result}") & i += 1:false
    end
  end
end

def set_die()
  #Investigating to see if the selected die is a valid "dietype"
  puts("Please select a die...")
  die = gets.chomp!
  die.downcase!
  case die
  when "d4", "d6", "d10", "d20", "d40"
  #if die == "d4" || "d6" || "d10" || "d20" || "d40"
    puts("#{die.upcase} selected...")
    puts($new_line)
    set_times(die)
  else
    puts("Invalid die! Please try again...")
    puts($new_line)
    set_die()
  end
end

def set_times(die)
  puts("Please select the number of times...")
  times = gets.chomp!
  puts($new_line)
  if times.to_i > 0
    create_event(die, times.to_i)
  elsif times == ""
    create_event(die)
  else
    puts("Invalid number, please use positive integers only.")
    set_times(die)
  end
end

def create_event(die, times=1)
  event = Dnd.new(die, times)
  event.roll_dice
  puts($new_line)
end

set_die()