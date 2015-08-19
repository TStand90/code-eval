def string_list(line)
  length, string = line.split(',')
  puts length
  puts string
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    string_list(line.chomp)
  end
end
