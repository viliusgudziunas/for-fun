puts "Please enter an integer:"
print ">"
int = gets.chomp.to_i

if int % 10 >= 8 || int % 10 == 0
  puts true
else
  puts false
end