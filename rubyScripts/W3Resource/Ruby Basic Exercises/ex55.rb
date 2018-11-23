puts "Please enter the following:"
print ">int1 = "
int1 = gets.chomp.to_i
print ">int2 = "
int2 = gets.chomp.to_i
print ">int3 = "
int3 = gets.chomp.to_i

c = [int1, int2, int3].max
a = [int1, int2, int3].min

if int1 == [int1, int2, int3].max
  if int2 == [int1, int2, int3].min
    b = int3
  elsif int3 == [int1, int2, int3].min
    b = int2
  end
end

if int2 == [int1, int2, int3].max
  if int1 == [int1, int2, int3].min
    b = int3
  elsif int3 == [int1, int2, int3].min
    b = int1
  end
end

if int3 == [int1, int2, int3].max
  if int1 == [int1, int2, int3].min
    b = int2
  elsif int2 == [int1, int2, int3].min
    b = int1
  end
end

first = (c - b).abs
second = (b - a).abs

if first == second
  puts true
else
  puts false
end