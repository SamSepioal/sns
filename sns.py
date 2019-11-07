def main():
    print("Hello world")

if __name__ == '__main__':
    st = SNSTopicCreator()
    testtasks = json.dumps({"email": "test123@gmail.com", "sms": "732-446-2386"})
    result, subscription_data = st._subscribe_topic_activity(testtaskjs)
