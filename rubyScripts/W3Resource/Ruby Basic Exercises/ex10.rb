puts "Please enter first integer:"
print ">"
int1 = gets.chomp.to_i

puts "Please enter second integer:"
print ">"
int2 = gets.chomp.to_i

puts "Please enter third integer:"
print ">"
int3 = gets.chomp.to_i

int1_in_range = int1 >= 1 && int1 <= 10
int2_in_range = int2 >= 1 && int2 <= 10
int3_in_range = int3 >= 1 && int3 <= 10

if int1_in_range && int2_in_range  && int3_in_range
  puts "All three integers are small"
elsif int1_in_range && int2_in_range
  puts "Only the first and second integers are small"
elsif int1_in_range && int3_in_range
  puts "Only the first and third integers are small"
elsif int2_in_range && int3_in_range
  puts "Only the second and third integers are small"
elsif int1_in_range
  puts "Only the first integer is small"
elsif int2_in_range
  puts "Only the second integer is small"
elsif int3_in_range
  puts "Only the third integer is small"
else
  puts "None of the integers are small"
end