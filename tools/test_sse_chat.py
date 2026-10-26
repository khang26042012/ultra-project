import urllib.request
import json
import sys

def main():
    req = urllib.request.Request(
        'http://localhost:3000/api/chat',
        data=json.dumps({
            'messages': [{'role': 'user', 'content': 'Cây sầu riêng của tôi bị xì mủ nâu ở gốc và vàng lá, bác sĩ chẩn đoán giúp tôi'}],
            'model': 'ag/gemini-3.8-flash-high'
        }).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )

    print('Connecting to /api/chat SSE endpoint...')
    tools_called = []
    full_text = ''
    full_thought = ''

    try:
        with urllib.request.urlopen(req, timeout=90) as res:
            for line in res:
                line_str = line.decode('utf-8', errors='ignore').strip()
                if not line_str.startswith('data: '):
                    continue
                payload = line_str[6:].strip()
                if payload == '[DONE]':
                    break
                try:
                    ev = json.loads(payload)
                    ev_type = ev.get('type')
                    if ev_type:
                        tools_called.append(f"{ev_type}: {str(ev)[:60]}")
                    elif ev_type == 'thought':
                        full_thought += ev.get('token', '')
                    elif ev_type == 'content':
                        full_text += ev.get('token', '')
                    elif ev_type == 'done':
                        print('-> [EVENT] Done stream signal received.')
                except Exception:
                    pass
    except Exception as e:
        print('Request error:', e)
        return

    print('=' * 60)
    print(f'Tools called ({len(tools_called)}):', tools_called)
    print(f'Thought length: {len(full_thought)} characters')
    print(f'Assistant reply length: {len(full_text)} characters')
    print('-' * 60)
    print('Preview response:')
    print(full_text[:600])
    print('=' * 60)

if __name__ == '__main__':
    main()
