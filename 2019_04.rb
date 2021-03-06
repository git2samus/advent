#!/usr/bin/env ruby

min_pwd, max_pwd = ARGF.read.split("-").map { |word| word.to_i }

puts (min_pwd..max_pwd).filter { |pwd|
  pwd.to_s.each_char.each_cons(2).all? { |a, b| a <= b }
}.filter { |pwd|
  pwd.to_s.each_char.each_cons(2).any? { |a, b| a == b }
}.count
