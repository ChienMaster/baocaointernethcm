import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Page title
st.set_page_config(page_title='ACOM CORP', page_icon='💻')
st.title('💻 Config to OLT ACOM')
st.info('Cấu hình tự động OLT các dự án của ACOM trên toàn quốc và kiểm tra số lượng thuê bao đang tồn tại.')


# Main content
tabs = st.tabs(['Cấu hình', 'Check thông tin dự án'])

with tabs[0]:
    project_options = ['Vinhomes Grand Park PK2', 'Vinhomes Grand Park PK3', 'Lavida Plus', 'Lux5 Bason', 'EcoxuanBD', 'TCL Tham Lương', 'HP One', 'AriaVT', 'BaryaVT', 'Hacom', 'Global City', 'Vin Hưng Yên', 'Vin Tây Mỗ', 'Vin Bắc Giang']
    selected_project = st.selectbox('Chọn dự án', project_options)

    if selected_project:
        st.write(f'Bạn đã chọn dự án: {selected_project}')
        st.write('Đang chuyển đến giao diện cấu hình OLT...')
        # TODO: Thêm logic để chuyển đến giao diện cấu hình OLT

with tabs[1]:
    recent_ticket_number = int(max(st.session_state.df.ID).split('-')[1])
    st.write(f'Số lượng thuê bao hiện tại: {recent_ticket_number - 1000}')
