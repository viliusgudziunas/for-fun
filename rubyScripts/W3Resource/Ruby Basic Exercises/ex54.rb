puts "Please enter the following:"
print ">x = "
x = gets.chomp.to_i
print ">y = "
y = gets.chomp.to_i
print ">z = "
z = gets.chomp.to_i

if (y.abs - z.abs).abs <= 1
  if (y.abs - x.abs).abs >= 3 && (z.abs - x.abs).abs >= 3
    puts true
  else
    puts false
  end
else
  puts false
end