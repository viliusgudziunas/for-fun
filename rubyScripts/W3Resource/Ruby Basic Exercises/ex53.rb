puts "Please enter the following:"
print ">int1 = "
int1 = gets.chomp.to_i
print ">int2 = "
int2 = gets.chomp.to_i
print ">int3 = "
int3 = gets.chomp.to_i

if int1 == 17
  puts 0
  exit
elsif int2 == 17
  puts int1
  exit
elsif int3 == 17
  puts int1 + int2
  exit
end

puts int1 + int2 + int3