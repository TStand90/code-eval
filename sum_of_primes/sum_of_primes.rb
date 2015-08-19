def prime_finder(number)
  (2...number).each do |y|
    if number % y == 0
      return false
	end
  end

  return true
end

sum_of_primes = 2
x = 3
primes_counter = 2

while primes_counter <= 1000 do
  if prime_finder(x)
    sum_of_primes += x
	primes_counter += 1
  end
  
  x += 1
end

puts(sum_of_primes)
