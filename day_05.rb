#!/usr/bin/env ruby
require 'digest'

door_id = ARGV[0]

n = 0
password = ""

md5 = Digest::MD5.new

while password.length < 8
  hash = md5.hexdigest("#{door_id}#{n}")
  password += hash[5] if hash.start_with?('00000')
  n += 1
end

puts password
