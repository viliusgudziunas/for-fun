puts "Please enter a string:"
print ">"
str = gets.chomp.downcase

if str[0, 2] == "if"
  puts "True"
else
  puts "False"
end