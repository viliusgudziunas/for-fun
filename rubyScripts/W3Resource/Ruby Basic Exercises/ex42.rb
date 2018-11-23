puts "Please enter a big integer:"
print ">"
num = gets.chomp
array = num.split("").map(&:to_i)

count = 0
array.each_with_index do |num, index|
  if index < 5
    if num == 7
      count += 1
    end
  else
    break
  end
end

if count > 0
  puts true
else
  puts false
end