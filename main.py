import requests
import time

# Your Telegram Bot Token
TOKEN = "x"

# Your Telegram Channel Chat ID
CHANNEL_CHAT_ID = "@channel"

# Function to send a message to the channel and delete it after 5 seconds
def send_and_delete_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_CHAT_ID,
        "text": "Ⓘ You have been mentioned by the channel owner.",
    }

    response = requests.post(url, data=data)
    message_id = response.json().get("result", {}).get("message_id")

    if message_id:
        time.sleep(5)
        delete_url = f"https://api.telegram.org/bot{TOKEN}/deleteMessage"
        delete_data = {
            "chat_id": CHANNEL_CHAT_ID,
            "message_id": message_id,
        }
        requests.post(delete_url, data=delete_data)

# Main loop to send and delete messages every 8 hours
while True:
    send_and_delete_message()
    # Sleep for 8hs (28800 seconds) before sending the next message
    time.sleep(28800)
