import matplotlib.pyplot as plt
from io import BytesIO
import streamlit as st
from matplotlib import font_manager

# 日本語フォントの設定
font_path = "./msgothic.ttc"# 使用するフォントファイルのパス
font_prop = font_manager.FontProperties(fname=font_path)

# Streamlitアプリの設定
st.title("日本語テキストを画像として保存")

# ユーザー入力
text = st.text_input("画像に変換する日本語テキストを入力してください:", "こんにちは、世界！")

# テキストを画像に変換する関数
def text_to_image(text):
    fig, ax = plt.subplots(figsize=(6, 3))  # 画像サイズを設定
    ax.text(0.5, 0.5, text, ha='center', va='center', fontsize=20, fontproperties=font_prop)
    ax.axis('off')  # 軸を非表示にする

    # 画像をBytesIOオブジェクトに保存
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=300)
    buf.seek(0)
    return buf

# テキストを画像に変換
img = text_to_image(text)

# 画像の表示
st.image(img, caption="生成された画像")

# 画像のダウンロード
st.download_button(label="画像をダウンロード", data=img, file_name="japanese_text.png", mime="image/png")
