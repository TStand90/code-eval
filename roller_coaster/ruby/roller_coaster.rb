filename = ARGV[0]
f = File.open(filename, "r") do |f|
  f.each_line do |line|
    line.split(" ").each do |word|
	  word.split("").each do |char|
	  puts word
	end
  end
end
