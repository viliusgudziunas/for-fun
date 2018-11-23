puts "Please enter a string:"
print ">"
string = gets.chomp

puts string[-1] + string[1...-1] + string[0]