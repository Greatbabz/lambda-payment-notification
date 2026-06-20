import json
import os
from datetime import datetime

def lambda_handler(event, context):
    currency = os.environ.get('CURRENCY', 'NGN')
    amount = event.get('amount', 0)
    sender = event.get('sender', 'Unknown')
    recipient = event.get('recipient', 'Unknown')

    if amount <= 0:
        return {'statusCode': 400, 'body': json.dumps({'error': 'Invalid amount'})}

    notification = {
        'status': 'Payment Processed',
        'sender': sender,
        'recipient': recipient,
        'amount': f'{currency} {amount:,.2f}',
        'timestamp': datetime.now().isoformat(),
        'reference': f'TXN{datetime.now().strftime("%Y%m%d%H%M%S")}'
    }

    print(f'Payment processed: {json.dumps(notification)}')
    return {'statusCode': 200, 'body': json.dumps(notification)}
