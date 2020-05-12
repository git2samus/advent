#!/usr/bin/env ruby

File.open(ARGV[0]) do |f|
  inputs, outputs = {}, Hash.new { |h, k| h[k] = [] }
  commands, bots = {}, Hash.new { |h, k| h[k] = [] }
  queue = []

  f.each_line do |line|
    case
    when line.start_with?('value')
      match = line.match(/value (?<chip>\d+) goes to bot (?<bot_id>\d+)/)
      chip, bot_id = Integer(match['chip']), Integer(match['bot_id'])

      inputs[chip] = bot_id
    when line.start_with?('bot')
      match = line.match(/bot (?<bot_id>\d+) gives low to (?<low_type>bot|output) (?<low_value>\d+) and high to (?<high_type>bot|output) (?<high_value>\d+)/)
      bot_id = Integer(match['bot_id'])
      low_type, low_value = match['low_type'], Integer(match['low_value'])
      high_type, high_value = match['high_type'], Integer(match['high_value'])

      commands[bot_id] = {:low => {:type => low_type, :value => low_value}, :high => {:type => high_type, :value => high_value}}
    end
  end

  inputs.each do |chip, bot_id|
    bots[bot_id] << chip

    if bots[bot_id].length == 2
      queue.insert(0, bot_id)
    end
  end

  while queue.length > 0
    bot_id = queue.pop

    low_chip, high_chip = bots[bot_id].min, bots[bot_id].max
    bots[bot_id].clear

    puts bot_id if low_chip == 17 and high_chip == 61

    low_type = commands[bot_id][:low][:type]
    low_value = commands[bot_id][:low][:value]
    if low_type == 'output'
      outputs[low_value] << low_chip
    else
      bots[low_value] << low_chip

      if bots[low_value].length == 2
        queue.insert(0, low_value)
      end
    end

    high_type = commands[bot_id][:high][:type]
    high_value = commands[bot_id][:high][:value]
    if high_type == 'output'
      outputs[high_value] << high_chip
    else
      bots[high_value] << high_chip

      if bots[high_value].length == 2
        queue.insert(0, high_value)
      end
    end
  end
end
