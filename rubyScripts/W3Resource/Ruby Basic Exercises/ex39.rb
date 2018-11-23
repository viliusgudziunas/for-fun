puts "Please enter a string:"
print ">"
string = gets.chomp.downcase

if string.include?("i")
  puts true
else
  puts false
end