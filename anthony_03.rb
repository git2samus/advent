#!/usr/bin/ruby

def triangle_possible?(s1, s2, s3)
  (s1+s2) > s3 && (s1+s3) > s2 && (s2+s3) > s1
end

possible_count = 0
lines = []

File.foreach(ARGV[0]) { |line| lines << line.chomp }

lines.each do |line|
  (s1, s2, s3) = line.split.map(&:to_i)
  possible_count += 1 if triangle_possible?(s1, s2, s3)
end

puts possible_count

possible_count = 0

lines.each_slice(3) do |(l1, l2, l3)|
  (s1, s4, s7) = l1.split.map(&:to_i)
  (s2, s5, s8) = l2.split.map(&:to_i)
  (s3, s6, s9) = l3.split.map(&:to_i)
  possible_count += 1 if triangle_possible?(s1, s2, s3)
  possible_count += 1 if triangle_possible?(s4, s5, s6)
  possible_count += 1 if triangle_possible?(s7, s8, s9)
end

puts possible_count