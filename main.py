import streamlit as st
import numpy as np
import pandas as pd
# 画像表示
from PIL import Image
import time

st.title('Streamlit 超入門')

# テキスト表示
# st.write('DataFrame')


# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40],
# })

# st.write(df)


# 動的なテーブル
# st.dataframe(df,width=100,height=100)

# st.dataframe(df.style.highlight_max(axis=0))
# axis=0・・・列の指定
# axis=1・・・行の指定

# 静的なテーブル
# st.table(df.style.highlight_max(axis=0))


# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """


# 乱数のグラフ表示
# df = pd.DataFrame(
#     np.random.rand(20,3),
#     # 縦に20行、横に3列
#     columns=['a','b','c']
# )

# st.line_chart(df)
#st.area_chart(df)
# st.bar_chart(df)


# 地図表示
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     # 縦に100行、横に2列
#     # [35.69,139.70]新宿付近
#     columns=['lat','lon']
#     # 緯度、経度
# )

# st.map(df)




# st.write('Display Image')
# img = Image.open('sample.jpg')
# st.image(img,caption='あすか会議2023',use_column_width=True)



# st.write('Interactive Widgets')

# チェックボックス
# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img,caption='あすか会議2023',use_column_width=True)

#セレクトボックス
# option = st.selectbox(
#     'あなたが好きな数字を教えてください。',
#     list(range(1,11))
# )

# 'あなたが好きな数字は' , option ,'です。'

# テキスト入力
# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：' , text

#スライダー
# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション：',condition



# サイドバー
# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：' , text
# 'コンディション：',condition


#2カラム
# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')


# expander
# expander1 = st.expander('問い合わせ1')
# expander1.write('お問い合せ1の回答')
# expander2 = st.expander('問い合わせ2')
# expander2.write('お問い合せ2の回答')
# expander3 = st.expander('問い合わせ3')
# expander3.write('お問い合せ3の回答')


# プログレスバー
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
    # ↑0.1は秒数指定

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('お問い合せ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('お問い合せ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('お問い合せ3の回答')


