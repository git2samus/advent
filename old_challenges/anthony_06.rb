#!/usr/bin/ruby

lines = []
File.foreach(ARGV[0]) { |line| lines << line.chomp }

rotated_lines = lines.map(&:chars).transpose
most_frequent_chars = rotated_lines.map do |chars|
  chars.sort.chunk(&:ord).to_a.sort_by { |_, arr| -arr.length }.map { |_, arr| arr.first}.first
end
puts most_frequent_chars.join
least_frequent_chars = rotated_lines.map do |chars|
  chars.sort.chunk(&:ord).to_a.sort_by { |_, arr| arr.length }.map { |_, arr| arr.first}.first
end
puts least_frequent_chars.join