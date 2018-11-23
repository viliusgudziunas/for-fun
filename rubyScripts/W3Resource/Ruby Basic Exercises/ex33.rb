puts "Please enter a year:"
print ">"
year = gets.chomp.to_i

if year % 4 == 0
  if year % 100 == 0
    if year % 400 ==0
      puts "Leap year"
    else
      puts "Not a leap year"
    end
  else
    puts "Leap year"
  end
else
    puts "Not a leap year"
end