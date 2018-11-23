puts "Please enter the following:"
print ">int1 = "
int1 = gets.chomp.to_i
print ">int2 = "
int2 = gets.chomp.to_i
print ">int3 = "
int3 = gets.chomp.to_i

if int1 == int2 && int1 == int3
  puts 0
  exit
end

if int1 == int2
  puts int3
  exit
elsif int1 == int3
  puts int2
  exit
elsif int2 == int3
  puts int1
  exit
end

puts int1 + int2 + int3