import requests
from bs4 import BeautifulSoup

# Steamの特価ページURL
url = "https://store.steampowered.com/search/?specials=1"
# User-Agentを指定してリクエスト（これがないと正しいHTMLが取得できない場合が多い）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

# BeautifulSoupでHTMLをパース
# 第1引数：response.content（取得したWebページのHTMLバイト列）
# 第2引数：'html.parser'（Python標準のHTMLパーサー。lxmlやhtml5libも指定可能）
soup = BeautifulSoup(response.content, 'html.parser')

# ゲームカード（1つ1つのゲーム情報が入っているaタグ）を全て取得
# class_='search_result_row'はSteamの検索・特価ページで使われているクラス名
# これで各ゲームの情報をまとめて取得できる
game_cards = soup.find_all('a', class_='ds_collapse_flag')
print(f"{len(game_cards)}個のゲームカードを取得")

# 最初の3つのゲームについて、タイトル・画像・リンクを表示
for card in game_cards[:3]:
    # ゲームタイトルを取得
    title_elem = card.find('span', class_='title')
    title = title_elem.get_text(strip=True) if title_elem else "タイトル不明"
    
    # ゲーム画像URLを取得
    img_elem = card.find('img')
    img_url = img_elem['src'] if img_elem else ""
    
    # ゲームページへのリンクを取得
    game_url = card['href']
    
    # 結果を表示
    print(f"タイトル: {title}")
    print(f"画像URL: {img_url}")
    print(f"リンク: {game_url}\n")  