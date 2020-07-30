from mycroft import MycroftSkill, intent_file_handler


class OpaTestTwo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('two.test.opa.intent')
    def handle_two_test_opa(self, message):
        self.speak_dialog('two.test.opa')


def create_skill():
    return OpaTestTwo()

