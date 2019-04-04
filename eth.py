import urllib
from bs4 import BeautifulSoup
import sys

def calc_profits(hash_rate, pwr_usage, kwh_cost, t_delta):
    source = 'http://coinmarketcap.com/currencies/ethereum/'
    r = urllib.urlopen(source)
    soup = BeautifulSoup(r, 'lxml')
    curr_price = float(str(soup.find("span", {"class":"text-large"}))[26:31])

    network_rate = 2.3 * (10**12)
    block_reward = 5.0
    network_block_rate = 24 * 60 * 4.1
    prob_block = hash_rate / network_rate

    pwr_costs = (24 * pwr_usage / 1000) * kwh_cost
    
    return ((network_block_rate * prob_block * block_reward * curr_price) - pwr_costs) * t_delta

print "Current profit projection: $%4.2f over %d days." % (calc_profits(42.0*10**6, 600., 0.129, float(sys.argv[1])), int(sys.argv[1]))
