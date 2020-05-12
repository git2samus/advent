#!/usr/bin/env ruby

File.open(ARGV[0]) { |f|
  puts f.each_line.map { |line|
    parts = line.split('-')
    name = parts[0..-2].join
    room_id, checksum = /(\d+)\[(\w+)\]/.match(parts[-1]).captures
    [name, checksum, room_id]
  }.select { |name, checksum, room_id|
    count = name.scan(/\w/).inject(Hash.new(0)) { |h, c|
      h[c] += 1
      h
    }.to_a.sort { |a, b|
      (b[1] == a[1])? a[0] <=> b[0] : b[1] <=> a[1]
    }

    checksum.split('').each_with_index.all? { |char, index|
      char == count[index][0]
    }
  }.map { |name, checksum, room_id|
    Integer(room_id)
  }.reduce :+
}
