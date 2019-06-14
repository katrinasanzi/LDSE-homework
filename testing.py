import logging
import sys
import ldclient
import time

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

if __name__ == "__main__":
  ldclient.set_sdk_key("sdk-3b6da147-d4a0-4fc9-89d3-28a69f806949")

  user = {
    "key": "Unique ID",
    "firstName": "Katrina",
    "lastName": "Sanzi",
    "custom": {
      "groups": "beta_testers"
    }
  }
  show_feature = ldclient.get().variation("new-search-bar", user, False)

  if show_feature:
    print("Showing your feature")
  else:
    print("Not showing your feature")

  while  1:
    show_feature = ldclient.get().variation("new-search-bar", user, False)
    if show_feature:
      print("Showing your feature")
      break
    else:
      print("Not showing your feature")
      time.sleep(5)
  ldclient.get().close()
