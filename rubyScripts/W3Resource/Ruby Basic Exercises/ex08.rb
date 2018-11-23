puts "Please enter first integer:"
print ">"
int1 = gets.chomp.to_i

puts "Please enter second integer:"
print ">"
int2 = gets.chomp.to_i

int1_in_range = int1 >= 20 && int1 <= 30
int2_in_range = int2 >= 20 && int2 <= 30

if int1_in_range && int2_in_range
  puts "Both integers are in the range 20 to 30 inclusive"
elsif int1_in_range
  puts "Only the first integer is in the range 20 to 30 inclusive"
elsif int2_in_range
  puts "Only the second integer is in the range 20 to 30 inclusive"
else
  puts "Neither of the integers is in the range 20 to 30 inclusive"
end