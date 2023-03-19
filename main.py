import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import time
from datetime import datetime, timedelta

# Set your API token and channel name
client = WebClient(token=os.environ['SLACK_API_TOKEN'])
channel_name = "#general"

# Set the message you want to send
message_text = "Hello, world!"

# Set the time you want to schedule the message
scheduled_time = datetime.now() + timedelta(minutes=5)

# Format the scheduled time as a Unix timestamp
scheduled_time_unix = int(scheduled_time.timestamp())

# Call the chat.scheduleMessage API method to schedule the message
try:
    result = client.chat_scheduleMessage(
        channel=channel_name,
        text=message_text,
        post_at=scheduled_time_unix
    )
    print(f"Scheduled message at {scheduled_time}: {result['message']['text']}")
except SlackApiError as e:
    print(f"Error scheduling message: {e}")

# Wait for the message to be sent
time.sleep(300)

# Call the chat.deleteScheduledMessage API method to delete the scheduled message
try:
    result = client.chat_deleteScheduledMessage(
        channel=channel_name,
        scheduled_message_id=result['scheduled_message_id']
    )
    print(f"Deleted scheduled message: {result}")
except SlackApiError as e:
    print(f"Error deleting scheduled message: {e}")
