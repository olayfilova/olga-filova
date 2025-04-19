#SINGLE RESPONSIBILITY
class Report:
    def generate_report(self, data):
        # Generate a report based on the provided data
        ...
        return report

    def transform_report(self, report):
        # Transform the generated report
        pass


class EmailProvider:
    def send_email(self, recipient, subject, body):
        # Send an email to the specified recipient
        pass

    def send_documents_by_email(self, documents):
        # Send documents to the specified recipient
        pass


class SendEmail:
    def send_email(self, recipient, subject, body):
        # Send an email to the specified recipient
        pass


class SendToTelegram:
    @staticmethod
    def send_to_telegram(self, message):
        # Send a message to Telegram
        pass


email_sender = EmailProvider()
report = Report.generate_report({})
email_sender.send_documents_by_email(report)
