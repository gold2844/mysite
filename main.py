import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ１')
expander1.write('問い合わせ１の回答')
expander2 = st.beta_expander('問い合わせ２')
expander2.write('問い合わせ２の回答')
expander3 = st.beta_expander('問い合わせ３')
expander3.write('問い合わせ３の回答')


# text = st.text_input('あなたに趣味を教えて下さい。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味は、',text
# 'コンディション：', condition

# option = st.selectbox(
#    'あなたが好きな数字を教えて下さい。',
#    list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'

# if st.checkbox('Shoow Image'):
#    img = Image.open('sample.jpg')
#    st.image(img, caption='Kouhei Imanishi', use_column_width=True)
