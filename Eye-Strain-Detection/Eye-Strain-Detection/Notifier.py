from plyer import notification

def notify():
    notification.notify(
        title="STRAIN ALERT",  # Title of the notification
        message="Reminder to Blink!",  # Message in the notification
        timeout=10,  # Duration for which the notification stays visible
        app_name="Eye Strain Detection",  # Optional app name for the notification
        toast=False  # Toast style (set it to True if you want it as a toast notification)
    )

