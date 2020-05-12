#!/usr/bin/env ruby

def fuel(mass)
  Enumerator.new do |enum|
    loop do
      mass = mass / 3 - 2
      enum << mass
    end
  end
end

puts ARGF.each_line.map { |line|
  line.to_i
}.map { |mass|
  fuel(mass).take_while { |fuel| fuel > 0 }.sum
}.sum
