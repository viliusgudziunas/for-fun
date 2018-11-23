puts "Please enter the following:"
print ">int1 = "
int1 = gets.chomp.to_i
print ">int2 = "
int2 = gets.chomp.to_i

if int1 < 10 || int2 < 10 || int1 > 99 || int2 > 99
  puts false
  exit
end

int1s = int1.to_s.split("")
int2s = int2.to_s.split("")

int1s.each do |char|
  int2s.each do |char1|
    if char == char1
      puts true
      exit
    end
  end
end

puts false