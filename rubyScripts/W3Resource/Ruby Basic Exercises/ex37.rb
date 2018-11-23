puts "Please enter an integer:"
print ">"
int1 = gets.chomp.to_i

puts "Please enter another integer:"
print ">"
int2 = gets.chomp.to_i

first = int1 >= 10 && int1 <= 20 || int1 >= 20 && int1 <= 30
second = int2 >= 10 && int2 <= 20 || int2 >= 20 && int2 <= 30

if first && second
  puts true
else
  puts false
end