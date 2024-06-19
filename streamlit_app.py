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
        options = ['Config', 'Check', 'Clear', 'Reboot', 'Bridge', 'thoai', 'iptv']
        st.write(f'Bạn đã chọn dự án: {selected_project}')
        st.write('Đang chuyển đến giao diện cấu hình OLT...')
        congthuc = st.text_area('Nhập công thức theo hướng dẫn của Chiến ACOM (Nếu không biết vui lòng liên hệ: 0932277923 Phone/Zalo Chiến ACOM)')
        if selected_project == 'Vinhomes Grand Park PK2':
            choice = st.selectbox('Bạn muốn gì?', options)
            if choice:
                st.write('Bạn muốn {} OLT Vinhomes Grand Park PK2'.format(choice))

with tabs[1]:
    recent_ticket_number = int(max(st.session_state.df.ID).split('-')[1])
    st.write(f'Số lượng thuê bao hiện tại: {recent_ticket_number - 1000}')
