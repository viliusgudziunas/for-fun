puts "Please enter the following:"
print ">int1 = "
int1 = gets.chomp.to_i
print ">int2 = "
int2 = gets.chomp.to_i
print ">int3 = "
int3 = gets.chomp.to_i

a = (int1 - int2).abs
b = (int1 - int3).abs
c = (int2 - int3).abs

if a >= 20 || b >= 20 || c >= 20
  puts true
else
  puts false
end