#!/usr/bin/ruby

100.times do |i|
  if (i % 3 == 0) and (i % 5 == 0) 
    print "fizzbuzz"
  elsif(i % 3 == 0) 
    print "fizz"
  elsif(i % 5 == 0) 
    print "buzz"
  else 
    print i
  end
  print "\n"
end
