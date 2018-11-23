marks = {:Literature => 74,
         :Science => 89,
         :Math => 91}

sum = 0
marks.each_value do |value|
  sum =+ sum + value
end

puts "Total marks: #{sum}"