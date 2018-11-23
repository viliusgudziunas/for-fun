puts "Please enter an integer:"
print ">"
num1 = gets.chomp.to_i

puts "Please enter a second integer:"
print ">"
num2 = gets.chomp.to_i

if num1 == 20 || num2 == 20
  puts "true"
else
  puts num1 * num2
end