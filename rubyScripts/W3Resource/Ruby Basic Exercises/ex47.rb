puts "Please enter the following:"
print ">int1 = "
int1 = gets.chomp.to_i
print ">int2 = "
int2 = gets.chomp.to_i
print ">int3 = "
int3 = gets.chomp.to_i

if int1 + int2 == int3 || int1 + int3 == int2 || int2 + int3 == int1
  puts true
else
  puts false
end