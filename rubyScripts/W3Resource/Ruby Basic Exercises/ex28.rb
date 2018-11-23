puts "Odd numbers between 10 and 1:"
10.step 1, -1 do |num|
  if num % 2 != 0
    puts num
  end
end