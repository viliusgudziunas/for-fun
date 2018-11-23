puts "Please enter a string:"
print ">"
string = gets.chomp
l_string = string.downcase

if l_string[0, 2] == "if"
  puts string
else
  puts "if #{string}"
end