puts "Please enter a string;"
print ">"
string = gets.chomp

new_string = ""

string.split("").each_with_index do |char, index|
  new_string = new_string + char unless index % 2 != 0
end

puts new_string