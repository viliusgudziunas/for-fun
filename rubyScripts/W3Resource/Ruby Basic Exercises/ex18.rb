puts "Please enter a number:"
print ">"
num1 = gets.chomp.to_f

puts "Please enter a second number:"
print ">"
num2 = gets.chomp.to_f

if num1 < num2
  puts "Max: #{num2}"
else
  puts "Max: #{num1}"
end