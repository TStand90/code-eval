f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    puts(line.downcase)
  end
end
