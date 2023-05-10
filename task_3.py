#2
casino_blacklist = {"Terry Stewart", "Cynthia Ramirez", "Jordan Gray", "Breanna Sims", "Anita Cook", "Brittany Mason"}
poker_blacklist = {"Richard Shields", "Breanna Sims", "James Collins", "Anita Cook", "Terry Stewart"}
alcohol_blacklist = {"Terry Stewart", "Steven Warren", "Matthew Collins", "Richard Pena", "Anita Cook"}
black_list = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(black_list)