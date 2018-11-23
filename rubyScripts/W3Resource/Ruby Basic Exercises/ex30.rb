puts "Please enter a non-negative integer:"
print ">"
int1 = gets.chomp

puts "Please enter another non-negative integer:"
print ">"
int2 = gets.chomp

if int1[-1] == int2[-1]
  puts true
else
  puts false
end