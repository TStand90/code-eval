def age_categorizer(age)
  if (0..2).include? age
    puts("Still in Mama's arms")
  elsif (3..4).include? age
    puts("Preschool Maniac")
  elsif (5..11).include? age
    puts("Elementary school")
  elsif (12..14).include? age
    puts("Middle school")
  elsif (15..18).include? age
    puts("High school")
  elsif (19..22).include? age
    puts("College")
  elsif (23..65).include? age
    puts("Working for the man")
  elsif (66..100).include? age
    puts("The Golden Years")
  else
    puts("This program is for humans")
  end
end

f = File.open(ARGV[0], "r") do |file|
  file.each_line do |line|
    age_categorizer(line.to_i)
  end
end
