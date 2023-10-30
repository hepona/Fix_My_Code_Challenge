###
#
#  Sort integer arguments (ascending)
#
###

result = []
ARGV.each do |arg|
    # skip if not integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    i_arg = arg.to_i

    # insert result at the right position
    if result.empty?
        result << i_arg
    else
        index = 0
        while index < result.size
            break if result[index] > i_arg
            index += 1
        end
        result.insert(index, i_arg)
    end
end

puts result
