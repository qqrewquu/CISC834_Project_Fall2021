import sys
import location, time
import urllib, webbrowser

# Handle argument, if present.
try:
	a = sys.argv[1]
except IndexError:
	a = ''

# Get the GPS info.
location.start_updates()
time.sleep(5)
loc = location.get_location()
addr = location.reverse_geocode(loc)
location.stop_updates()

# Assemble the output.
spot = '''%s%s
%s, %s %s
%.4f, %.4f''' % \
  (a, addr[0]['Street'],
   addr[0]['City'], addr[0]['State'], addr[0]['ZIP'],
   loc['latitude'], loc['longitude'])

# Send output to Drafts.
webbrowser.open("drafts://x-callback-url/create?text=" + urllib.quote(spot.encode('utf-8')))