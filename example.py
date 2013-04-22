from tesla import TeslaMotors

t = TeslaMotors(username='', password='')

# Forum topic for members only
r = t.get_page('http://www.teslamotors.com/forum/forums/prioritized-software-enhancement-list')
print r.content