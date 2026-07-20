import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

cards_dir = r'D:\open_work\Research\knowledge-base\卡片'

for f in sorted(os.listdir(cards_dir)):
    if not f.endswith('.md'):
        continue
    filepath = os.path.join(cards_dir, f)
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    # Extract the 关联 section
    m = re.search(r'##\s*关联\n(.*?)(?=\n##\s|\Z)', content, re.DOTALL)
    if not m:
        continue
    
    card_name = f[:-3]
    links_text = m.group(1).strip()
    if not links_text:
        continue
    
    print(f'\n===== {card_name} =====')
    print(links_text)
