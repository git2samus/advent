#!/usr/bin/env ruby

File.open(ARGV[0]) { |f|
  input = f.read.strip

  scan_index, uncompressed_length = 0, 0
  compression_pattern = /\((\d+)x(\d+)\)/

  while true
    matchpos = input.index(compression_pattern, scan_index)
    if matchpos.nil?
      uncompressed_length += input.length - scan_index
      break
    end

    match = input.match(compression_pattern, scan_index)
    chars, reps = match.captures.map(&:to_i)

    uncompressed_length += (matchpos - scan_index) + (chars * reps)
    scan_index += (matchpos - scan_index) + (match[0].length + chars)
  end

  puts uncompressed_length
}
