puts "Please enter two temperatures:"

print ">temp1 = "
temp1 = gets.chomp.to_i
print ">temp2 = "
temp2 = gets.chomp.to_i

case
when temp1 < 0 && temp2 > 100 || temp2 < 0 && temp1 > 100
  puts true
else
  puts false
end