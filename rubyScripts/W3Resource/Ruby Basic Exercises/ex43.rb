puts "Please enter a big integer:"
print ">"
num = gets.chomp
array = num.split("").map(&:to_i)

new_array = []
array.each do |num|
  new_array.push(num * 10)
end

index = 0
while index < new_array.length - 2
  if new_array[index..index + 2] == [10, 20, 30]
    puts true
    exit
  end
  index += 1
end

puts false