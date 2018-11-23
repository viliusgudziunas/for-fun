puts "Please enter integer values for the following:"

print "num1 = "
num1 = gets.chomp.to_i
print "num2 = "
num2 = gets.chomp.to_i

case
when num1 == num2
  puts (num1 + num2) * 2
else
  puts (num1 + num2)
end