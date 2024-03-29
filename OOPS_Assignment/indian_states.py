'''Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.'''

import json

dict = {
  "Maharashtra": "Mumbai",
  "Karnataka": "Bengaluru",
  "Tamil Nadu": "Chennai",
  "Uttar Pradesh": "Lucknow",
  "Gujarat": "Gandhinagar",
  "Kerala": "Thiruvananthapuram",
  "Rajasthan": "Jaipur"
}

with open("indian_states.json", 'w') as file:
   json_object = json.dumps(dict, indent = 7)
   file.write(json_object)
