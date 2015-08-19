def n_mod_m(n, m)
  modulo = (n % m)
  modulo
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    n, m = line.split(',')
	n = n.to_i
	m = m.to_i
	puts(n_mod_m(n, m))
  end
end
