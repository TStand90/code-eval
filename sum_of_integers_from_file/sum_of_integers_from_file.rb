filename = ARGV[0]

sum = 0

f = File.open(filename, "r") do |file|
  file.each_line do |line|
    sum += line.to_i
  end
end

puts sum
