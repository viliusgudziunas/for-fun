puts "Please enter the following:"
print ">int1 = "
int1 = gets.chomp.to_i
print ">int2 = "
int2 = gets.chomp.to_i

first = int1 % 5
second = int2 % 5

if int1 == int2
  puts 0
  exit
end

if first == second
  if int1 > int2
    puts int2
    exit
  else
    puts int1
    exit
  end
end

if int1 > int2
  puts int1
else
  puts int2
end