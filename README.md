# Tweet Reservation Bot

このリポジトリでは、Tweet Reservation Botが提供されています。
Discordを通じて予約されたツイートを指定された時間にTwitterに投稿するDiscordボットです。

## 前提条件

- Python 3.8以上
- Twitter DeveloperアカウントとAPIキー
- Discord DeveloperアカウントとBotトークン
- インストール済みの必要なPythonライブラリ:
  - discord.py
  - tweepy
  - python-dotenv

## セットアップ手順

1. このリポジトリをクローンまたはダウンロードして、ローカルマシンに保存します。
2. 必要なPythonライブラリをインストールします:
```
pip install discord.py tweepy python-dotenv
```

3. ルートディレクトリに.envファイルを作成し、以下の環境変数を設定します:
```
DISCORD_BOT_TOKEN=your_discord_bot_token
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET_KEY=your_twitter_api_secret_key
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
```

4. `tweet_reservation.py`スクリプトを実行して、ボットを起動します:
```
python tweet_reservation.py
```

5. DiscordサーバーにBotを招待し、必要な権限を付与します。
6. `!tweet`コマンドを使用して、予約されたツイートをスケジュールします。例:
```
!tweet 2023,03,19,8,44 予約ツイートのテストです！
```

## コマンド

- `!tweet <timestamp> <tweet_text>`: タイムスタンプ（形式：`YYYY,MM,DD,HH,MM`）で指定された時間に、`<tweet_text>`で指定されたテキストをツイートします。予約が成功すると、予約確認メッセージを送信します。

## 注意

- 予約されたツイートは、指定されたタイムスタンプが現在時刻よりも未来である場合にのみスケジュールされます。
- タイムスタンプの形式が正しくない場合、エラーメッセージが表示されます。

## ライセンス

MIT License

## 貢献
バグ報告や機能追加のリクエストは、GitHubのイシューでお願いします。プルリクエストも歓迎します。