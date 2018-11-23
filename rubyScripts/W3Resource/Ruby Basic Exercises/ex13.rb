puts "Please enter a string:"
print ">"
string = gets.chomp

puts "Please enter a non-negative integer:"
print ">"
int = gets.chomp.to_i

puts string[0..2] * int