class User:
    def __init__(self, username, engagement):
        self.name = username
        self.engagement_metrics = engagement
    
    def __repr__(self) -> str:
        return f"User {self.name}"


def get_user_score(user: User):
    try:
        return perform_calculation(user.engagement_metrics)
    except KeyError:
        print("Incorrect values provided to our calculation function")
        raise
    # else:
    #     send_engagement_notification(user) In case we want to send a message if an error was not cached


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics["hits"] * 2


def send_engagement_notification(user):
    print(f'Notification sent to {user}')


if __name__ == "__main__":
    my_user = User('Rolf', {'clicks': 61,
                            'hits': 100})
    get_user_score(user=my_user)
