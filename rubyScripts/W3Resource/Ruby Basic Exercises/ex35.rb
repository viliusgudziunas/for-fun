puts "Please enter a string:"
print ">"
string = gets.chomp
string1 = string.downcase

if string1[0..1] == "ps"
  puts "ps"
else
  puts ""
end