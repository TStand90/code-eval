def number_of_ones(binary)
  binary.count("1")
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    integer = line.to_i
	binary = integer.to_s(2)
	puts(number_of_ones(binary))
  end
end
