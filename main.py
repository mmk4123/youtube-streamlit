import streamlit as st
import time
#import numpy as np
#import pandas as pd
#from PIL import Image


st.title('Streamlit 超入門')


st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'



left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander1 = st.beta_expander('問い合わせ2')
expander1.write('問い合わせ2の回答')
expander1 = st.beta_expander('問い合わせ3')
expander1.write('問い合わせ3の回答')



if st.checkbox('show Image'):
    img=Image.open('LP2.png')
    st.image(img,caption='Kohei Imanishi',use_column_width=True)

option = st.selectbox(
    'あなたは好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は', option ,'です。'




text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は?',0,100,50)

'あなたの趣味', text
'コンディション',condition





st.write('Hello, *World!* :sunglasses:') # 絵文字も使える

df=pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})


st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)



"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""