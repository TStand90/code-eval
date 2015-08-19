filename = ARGV[0]

def fibo(number)
  if number == 1 or number == 2
    1
  elsif number == 0
    0
  else
    fibo(number - 2) + fibo(number - 1)
  end
end

f = File.open(filename, "r") do |file|
  file.each_line do |line|
    number = line.to_i
	puts(fibo(number))
  end
end
