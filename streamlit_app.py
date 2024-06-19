import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Page title
st.set_page_config(page_title='ACOM CORP', page_icon='💻')
st.title('💻 Config to OLT ACOM')
st.info('Cấu hình tự động OLT các dự án của ACOM trên toàn quốc và kiểm tra số lượng thuê bao đang tồn tại.')

start_date = datetime(2023, 6, 1)
end_date = datetime(2023, 12, 20)
id_values = ['TICKET-{}'.format(i) for i in range(1000, 1100)]
issue_list = [generate_issue() for _ in range(100)]


def generate_random_dates(start_date, end_date, id_values):
    date_range = pd.date_range(start_date, end_date).strftime('%m-%d-%Y')
    return np.random.choice(date_range, size=len(id_values), replace=False)

## Generate 100 rows of data
data = {'Issue': issue_list,
        'Status': np.random.choice(['Open', 'In Progress', 'Closed'], size=100),
        'Priority': np.random.choice(['High', 'Medium', 'Low'], size=100),
        'Date Submitted': generate_random_dates(start_date, end_date, id_values)
    }
df = pd.DataFrame(data)
df.insert(0, 'ID', id_values)
df = df.sort_values(by=['Status', 'ID'], ascending=[False, False])

## Create DataFrame
if 'df' not in st.session_state:
    st.session_state.df = df



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
