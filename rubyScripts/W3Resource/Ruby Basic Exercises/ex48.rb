puts "Please enter the following:"
print ">int1 = "
int1 = gets.chomp.to_i
print ">int2 = "
int2 = gets.chomp.to_i
print ">int3 = "
int3 = gets.chomp.to_i

if int1 % 10 == int2 % 10 || int1 % 10 == int3 % 10 || int2 % 10 == int3 % 10
  puts true
else
  puts false
end