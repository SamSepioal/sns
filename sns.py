def main():
    print("Hello world")

class SNSTopicShell:
    def fail(self, reason):
        print(reason)

    def complete(self, result):
        print(result)

class SNSTopicCreator(SNSTopicShell):
    def create_topic(self, client):
        t = client.create_topic('SNS Messaging Stuff')
        print(t)
        topic_arn = t['CreateTopicResponse']['CreateTopicResult']['TopicArn']

        if topic_arn:
            client.set_topic_attributes(topic_arn, 'DisplayName', 'SNSample')
        else:
            self.fail(reason=json.dumps({"reason", "Couldn't create SNS topic", "detail", ""}))
            return False, "Couldn't create SNS topic"
        return True, topic_arn

if __name__ == '__main__':
    st = SNSTopicCreator()
    testtasks = json.dumps({"email": "test123@gmail.com", "sms": "732-446-2386"})
    result, subscription_data = st._subscribe_topic_activity(testtaskjs)
